# -*- coding: utf-8 -*-
import json
import re

def parse_text():
    with open('extracted_reader.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Trim and clean lines
    lines = [l.strip() for l in lines]
    
    # Let's extract the main sections
    # 1. Intro
    # 2. Table of destinations
    # 3. Brisbane
    # 4. Gold Coast
    # 5. Sydney
    # 6. Challenge
    
    book = {
        "title": "MY AUSTRALIA TRAVEL BOOK",
        "subtitle": "我的澳洲旅行小書",
        "intro_title": "如何使用這本小讀本 How to Use This Book",
        "intro_zh": "",
        "intro_en": "",
        "table_title": "我們要去哪裡？ Where Are We Going?",
        "cities": []
    }
    
    # Read lines manually to extract sections
    i = 0
    # Header lines
    while i < len(lines):
        if "如何使用這本小讀本" in lines[i]:
            break
        i += 1
    
    # Intro content
    if i < len(lines):
        i += 1 # Skip title line
        zh_parts = []
        en_parts = []
        # Next lines until "我們要去哪裡"
        while i < len(lines) and "我們要去哪裡" not in lines[i]:
            line = lines[i]
            if line:
                if any('\u4e00' <= char <= '\u9fff' for char in line):
                    # Contains Chinese
                    # Check if it also contains English
                    if re.search(r'[a-zA-Z]{3,}', line):
                        # Both, let's split or keep as is
                        zh_parts.append(line)
                    else:
                        zh_parts.append(line)
                else:
                    en_parts.append(line)
            i += 1
        book["intro_zh"] = " ".join(zh_parts)
        # Separate zh and en from line 8
        # "每個景點都有中文故事、簡易英文與趣味小知識。旅行前可以先讀，抵達景點後再找找看書中提到的建築、動物或歷史線索。"
        # "Each place has a Chinese story, simple English, and a fun fact..."
        book["intro_zh"] = "每個景點都有中文故事、簡易英文與趣味小知識。旅行前可以先讀，抵達景點後再找找看書中提到的建築、動物或歷史線索。"
        book["intro_en"] = "Each place has a Chinese story, simple English, and a fun fact. Read it before the trip, then look for the buildings, animals, and clues when you arrive."

    # Skip to Brisbane
    while i < len(lines):
        if "第一站" in lines[i]:
            break
        i += 1
        
    current_city = None
    
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
            
        # Check for city header
        if "第一站：布里斯本" in line or "第一站" in line:
            current_city = {
                "name_zh": "布里斯本",
                "name_en": "Brisbane",
                "tagline": "THE RIVER CITY",
                "desc_zh": lines[i+1],
                "desc_en": lines[i+2],
                "attractions": []
            }
            book["cities"].append(current_city)
            i += 3
            continue
        elif "第二站：黃金海岸" in line or "第二站" in line:
            current_city = {
                "name_zh": "黃金海岸",
                "name_en": "Gold Coast",
                "tagline": "BEACHES, RAINFOREST AND LIVING LIGHTS",
                "desc_zh": lines[i+1],
                "desc_en": lines[i+2],
                "attractions": []
            }
            book["cities"].append(current_city)
            i += 3
            continue
        elif "第三站：雪梨" in line or "第三站" in line:
            current_city = {
                "name_zh": "雪梨",
                "name_en": "Sydney",
                "tagline": "HARBOUR, HISTORY AND SANDSTONE",
                "desc_zh": lines[i+1],
                "desc_en": lines[i+2],
                "attractions": []
            }
            book["cities"].append(current_city)
            i += 3
            continue
        elif "旅行結束前的小挑戰" in line:
            break
            
        # Check for attraction
        match = re.match(r'^(\d+)\.\s*(.*)$', line)
        if match and current_city is not None:
            num = match.group(1)
            title = match.group(2)
            
            attraction = {
                "num": num,
                "title": title,
                "desc_zh": "",
                "desc_en": "",
                "fun_fact_zh": "",
                "fun_fact_en": "",
                "source": ""
            }
            
            # Now parse attraction details
            i += 1
            while i < len(lines):
                if not lines[i]:
                    i += 1
                    continue
                
                # If we hit another attraction or next section, break
                if re.match(r'^(\d+)\.', lines[i]) or "第" in lines[i] and "站" in lines[i] or "旅行結束前" in lines[i]:
                    break
                
                curr_line = lines[i]
                if curr_line == "中文介紹":
                    i += 1
                    attraction["desc_zh"] = lines[i]
                elif curr_line == "English":
                    i += 1
                    attraction["desc_en"] = lines[i]
                elif curr_line.startswith("趣味小知識"):
                    # Parse fun fact
                    text = curr_line.replace("趣味小知識 Fun Fact", "").replace("趣味小知識 Fun Fact ", "").strip()
                    # Find the transition where English text starts and goes to the end without containing Chinese characters
                    match = re.search(r'([A-Z][^\u4e00-\u9fff]*)$', text)
                    if match:
                        en_text = match.group(1).strip()
                        zh_text = text[:match.start()].strip()
                        attraction["fun_fact_zh"] = zh_text
                        attraction["fun_fact_en"] = en_text
                    else:
                        attraction["fun_fact_zh"] = text
                elif curr_line.startswith("資料來源"):
                    attraction["source"] = curr_line.replace("資料來源 ", "")
                
                i += 1
            
            current_city["attractions"].append(attraction)
            continue
            
        i += 1
        
    # Challenge section
    challenge_questions = []
    while i < len(lines):
        line = lines[i]
        if "旅行結束前的小挑戰" in line:
            i += 1
            continue
        if "Have a wonderful trip" in line or "祝你有一趟精彩" in line:
            break
        if line:
            # e.g. "為什麼故事橋叫Story Bridge？ Why is Story Bridge called Story Bridge?"
            # Split zh and en
            split_match = re.search(r'([A-Z][^\u4e00-\u9fff]*)$', line)
            if split_match:
                en_q = split_match.group(1).strip()
                zh_q = line[:split_match.start()].strip()
                challenge_questions.append({"zh": zh_q, "en": en_q})
            else:
                challenge_questions.append({"zh": line, "en": ""})
        i += 1
        
    book["challenges"] = challenge_questions
    return book

if __name__ == '__main__':
    book_data = parse_text()
    with open('book_data.json', 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=2)
    print("Parsed data successfully saved to book_data.json")
