# -*- coding: utf-8 -*-
import json
import os

def build_html():
    with open('book_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Manual corrections for some fields
    # Q1: 為什麼故事橋叫Story Bridge？
    data["challenges"][0]["zh"] = "為什麼故事橋叫Story Bridge？"
    data["challenges"][0]["en"] = "Why is Story Bridge called Story Bridge?"
    
    html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Australia Travel Book - 我的澳洲旅行小書</title>
    <!-- Google Fonts: Fredoka for headings, Outfit for body text -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Outfit:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f5f3ef;
            --page-bg: #ffffff;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --brisbane-color: #0f766e;
            --brisbane-bg: #f0fdfa;
            --goldcoast-color: #b45309;
            --goldcoast-bg: #fffbeb;
            --sydney-color: #1d4ed8;
            --sydney-bg: #eff6ff;
            --border-radius: 12px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-dark);
            padding: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Screen Preview styles */
        .controls {
            margin-bottom: 20px;
            text-align: center;
            position: sticky;
            top: 20px;
            z-index: 100;
        }

        .btn-print {
            background-color: #059669;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            font-family: 'Fredoka', sans-serif;
        }

        .btn-print:hover {
            background-color: #047857;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
        }

        .book-container {
            display: flex;
            flex-direction: column;
            gap: 40px;
            align-items: center;
        }

        /* Page Layout - A4 Aspect Ratio on Screen */
        .page {
            width: 210mm;
            height: 297mm;
            background-color: var(--page-bg);
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
            padding: 15mm 15mm;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            border-radius: 4px;
        }

        /* Page Background Decoration */
        .page::before {
            content: '';
            position: absolute;
            top: 8mm;
            left: 8mm;
            right: 8mm;
            bottom: 8mm;
            border: 1px dashed #cbd5e1;
            pointer-events: none;
            border-radius: 8px;
            z-index: 1;
        }

        .page-header {
            font-family: 'Fredoka', sans-serif;
            font-size: 9pt;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1.5px solid #f1f5f9;
            padding-bottom: 4px;
            z-index: 10;
        }

        .page-header span.city-tag {
            font-weight: bold;
        }

        .page-footer {
            font-family: 'Fredoka', sans-serif;
            font-size: 9pt;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1.5px solid #f1f5f9;
            padding-top: 4px;
            z-index: 10;
        }

        .page-content {
            flex-grow: 1;
            padding: 6mm 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            z-index: 10;
            overflow: hidden;
        }

        /* Cover Page Custom Styling */
        .page.cover-page {
            justify-content: space-between;
            align-items: center;
            text-align: center;
            background: radial-gradient(circle at 10% 20%, #faf8f5 0%, #f4eae1 90%);
        }

        .page.cover-page::before {
            border: 3px double #d97706;
        }

        .cover-header {
            margin-top: 5mm;
        }

        .cover-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 34pt;
            font-weight: 700;
            color: #b45309;
            line-height: 1.1;
            margin-bottom: 5px;
        }

        .cover-subtitle {
            font-size: 22pt;
            font-weight: 700;
            color: #451a03;
            letter-spacing: 2px;
            margin-bottom: 12px;
        }

        .cover-cities {
            font-family: 'Fredoka', sans-serif;
            font-size: 14pt;
            color: var(--text-muted);
            letter-spacing: 1px;
            border-bottom: 2px solid #b45309;
            padding-bottom: 6px;
            margin-bottom: 10px;
            display: inline-block;
        }

        .cover-desc {
            font-size: 12pt;
            color: #78350f;
            font-weight: 500;
        }

        .cover-image-container {
            width: 100%;
            height: 110mm;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 5px solid white;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .cover-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .cover-footer {
            width: 85%;
            margin-bottom: 5mm;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }

        .name-box {
            width: 100%;
            padding: 8px;
            border: 2px dashed #b45309;
            border-radius: 8px;
            font-size: 13pt;
            font-weight: bold;
            color: #451a03;
            background-color: rgba(255,255,255,0.6);
        }

        /* Chapter Divider Page */
        .page.chapter-divider {
            justify-content: space-between;
            padding: 15mm;
        }

        .divider-title-group {
            text-align: center;
            margin-top: 2mm;
        }

        .divider-city-en {
            font-family: 'Fredoka', sans-serif;
            font-size: 36pt;
            font-weight: 700;
            line-height: 1;
        }

        .divider-city-zh {
            font-size: 24pt;
            font-weight: 700;
            margin-top: 5px;
        }

        .divider-tagline {
            font-family: 'Fredoka', sans-serif;
            font-size: 11pt;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 10px;
            font-weight: 600;
        }

        .divider-desc-box {
            margin: 15px 0;
            padding: 15px;
            border-radius: var(--border-radius);
            font-size: 11pt;
            line-height: 1.5;
        }

        .divider-desc-en {
            font-weight: 500;
            margin-bottom: 8px;
            font-size: 11.5pt;
        }

        .divider-desc-zh {
            color: var(--text-muted);
            border-top: 1px dashed rgba(0,0,0,0.1);
            padding-top: 8px;
            font-size: 10pt;
        }

        .divider-image-container {
            width: 100%;
            height: 105mm;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 4px solid white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            margin-bottom: 2mm;
        }

        .divider-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* Theme Styling for Dividers and Content Pages */
        .brisbane-theme {
            --theme-color: var(--brisbane-color);
            --theme-bg: var(--brisbane-bg);
        }
        .goldcoast-theme {
            --theme-color: var(--goldcoast-color);
            --theme-bg: var(--goldcoast-bg);
        }
        .sydney-theme {
            --theme-color: var(--sydney-color);
            --theme-bg: var(--sydney-bg);
        }

        .page.chapter-divider.brisbane-theme::before { border: 2px solid var(--brisbane-color); }
        .page.chapter-divider.goldcoast-theme::before { border: 2px solid var(--goldcoast-color); }
        .page.chapter-divider.sydney-theme::before { border: 2px solid var(--sydney-color); }

        .page.chapter-divider .divider-city-en { color: var(--theme-color); }
        .page.chapter-divider .divider-tagline { color: var(--text-muted); }
        .page.chapter-divider .divider-desc-box { background-color: var(--theme-bg); border-left: 5px solid var(--theme-color); }

        /* Intro Page Layout */
        .intro-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 16pt;
            color: #b45309;
            margin-bottom: 10px;
            border-bottom: 2px solid #fcd34d;
            padding-bottom: 4px;
        }

        .intro-box {
            background-color: #fffbeb;
            padding: 12px;
            border-radius: 8px;
            border-left: 4px solid #f59e0b;
            margin-bottom: 15px;
            font-size: 10.5pt;
            line-height: 1.5;
        }

        .intro-box-en {
            font-weight: 500;
            margin-bottom: 6px;
            font-size: 11pt;
            color: #78350f;
        }

        .intro-box-zh {
            color: #b45309;
            font-size: 9.5pt;
        }

        .table-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 15pt;
            color: #1e293b;
            margin-bottom: 10px;
        }

        /* Styled Table */
        .dest-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 10pt;
            margin-bottom: 15px;
        }

        .dest-table th {
            background-color: #f1f5f9;
            color: #1e293b;
            text-align: left;
            padding: 8px;
            font-weight: 700;
            border-bottom: 2px solid #cbd5e1;
        }

        .dest-table td {
            padding: 10px 8px;
            border-bottom: 1px solid #e2e8f0;
        }

        .dest-table tr:hover {
            background-color: #f8fafc;
        }

        .dest-city-cell {
            font-weight: bold;
            color: #b45309;
        }

        /* Attraction Item Styling - Layout 3 per Page */
        .attractions-list {
            display: flex;
            flex-direction: column;
            gap: 4mm;
            height: 100%;
            justify-content: space-between;
        }

        /* For 4 items on Sydney's last page, make gaps smaller */
        .attractions-list.four-items {
            gap: 2mm;
        }

        .attraction-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .attraction-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 13.5pt;
            font-weight: 700;
            color: var(--theme-color);
            border-bottom: 1.5px solid #f1f5f9;
            padding-bottom: 2px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .attraction-title span.number {
            background-color: var(--theme-color);
            color: white;
            border-radius: 50%;
            width: 22px;
            height: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10pt;
        }

        .attraction-desc-en {
            font-size: 11pt;
            font-weight: 500;
            line-height: 1.4;
            color: var(--text-dark);
            text-align: justify;
        }

        .attraction-desc-zh {
            font-size: 9pt;
            line-height: 1.35;
            color: var(--text-muted);
            text-align: justify;
        }

        .attraction-funfact {
            background-color: var(--theme-bg);
            border: 1.5px dashed #cbd5e1;
            border-radius: 8px;
            padding: 8px 10px;
            margin-top: 2px;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .funfact-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 9pt;
            font-weight: 700;
            color: var(--theme-color);
            display: flex;
            align-items: center;
            gap: 4px;
            text-transform: uppercase;
        }

        .funfact-text-en {
            font-size: 10pt;
            font-weight: 600;
            color: #0f172a;
            line-height: 1.3;
        }

        .funfact-text-zh {
            font-size: 8.5pt;
            color: var(--text-muted);
            line-height: 1.3;
        }

        .attraction-source {
            font-size: 7.5pt;
            color: var(--text-muted);
            text-align: right;
            font-style: italic;
            margin-top: 1px;
        }

        /* Challenge Page Styling */
        .challenge-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 18pt;
            color: #0f766e;
            text-align: center;
            margin-bottom: 12px;
            border-bottom: 2px solid #99f6e4;
            padding-bottom: 6px;
        }

        .challenge-intro {
            font-size: 10pt;
            color: var(--text-muted);
            text-align: center;
            margin-bottom: 15px;
        }

        .questions-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .question-card {
            background-color: #f0fdfa;
            border: 1px solid #ccfbf1;
            border-radius: 8px;
            padding: 10px 12px;
            position: relative;
        }

        .question-num {
            position: absolute;
            top: -9px;
            left: 12px;
            background-color: #0f766e;
            color: white;
            font-family: 'Fredoka', sans-serif;
            font-size: 8.5pt;
            font-weight: bold;
            padding: 1px 6px;
            border-radius: 10px;
        }

        .question-text-en {
            font-size: 11pt;
            font-weight: 600;
            color: #0f172a;
            margin-top: 3px;
            margin-bottom: 3px;
        }

        .question-text-zh {
            font-size: 9.5pt;
            color: #0d9488;
            margin-bottom: 5px;
        }

        .answer-line {
            width: 100%;
            height: 25px;
            border-bottom: 1px dashed #99f6e4;
            margin-top: 3px;
        }

        /* Back Cover Styling */
        .back-cover {
            background: radial-gradient(circle at 90% 80%, #faf8f5 0%, #eae1d8 90%);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
        }

        .back-cover::before {
            border: 3px double #0f766e;
        }

        .diary-section {
            width: 100%;
            margin-top: 5mm;
            text-align: left;
        }

        .diary-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 15pt;
            color: #0f766e;
            margin-bottom: 10px;
            border-bottom: 2px solid #99f6e4;
            padding-bottom: 4px;
        }

        .writing-lines {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 8px;
        }

        .writing-line {
            border-bottom: 1px dashed #cbd5e1;
            height: 22px;
        }

        .back-closing {
            margin-bottom: 5mm;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }

        .closing-banner {
            background-color: #0f766e;
            color: white;
            font-family: 'Fredoka', sans-serif;
            font-size: 14pt;
            font-weight: bold;
            padding: 8px 24px;
            border-radius: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .closing-sub {
            font-size: 12pt;
            font-weight: 700;
            color: #0f172a;
        }

        .stamp-decor {
            font-size: 20pt;
            margin-top: 5px;
        }

        /* Print styles */
        @media print {
            body {
                background-color: white;
                padding: 0;
                margin: 0;
            }

            .controls {
                display: none;
            }

            .book-container {
                gap: 0;
            }

            .page {
                box-shadow: none;
                page-break-after: always;
                width: 210mm;
                height: 297mm;
                margin: 0;
                border-radius: 0;
                padding: 15mm 15mm !important;
            }
            
            @page {
                size: A4;
                margin: 0;
            }
        }
    </style>
</head>
<body>

    <div class="controls">
        <button class="btn-print" onclick="window.print()">🖨️ 列印旅遊手冊 (Print Booklet)</button>
    </div>

    <div class="book-container">
"""
    
    # Page 1: Cover Page
    html += """
        <!-- PAGE 1: COVER PAGE -->
        <div class="page cover-page">
            <div class="cover-header">
                <h1 class="cover-title">MY AUSTRALIA</h1>
                <h2 class="cover-subtitle">TRAVEL BOOK</h2>
                <div class="cover-cities">Brisbane &middot; Gold Coast &middot; Sydney</div>
                <p class="cover-desc">我的澳洲旅行小書 · 中英文旅遊小讀本</p>
            </div>
            <div class="cover-image-container">
                <img src="images/cover.jpg" alt="Australia Cover" class="cover-image">
            </div>
            <div class="cover-footer">
                <div class="name-box">Traveler 小小旅行家: _________________</div>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 1</span>
            </div>
        </div>
    """
    
    # Page 2: Intro & Table
    html += f"""
        <!-- PAGE 2: INTRO & TOC -->
        <div class="page">
            <div class="page-header">
                <span>INTRODUCTION</span>
                <span>GETTING READY</span>
            </div>
            <div class="page-content">
                <h3 class="intro-title">{data['intro_title']}</h3>
                <div class="intro-box">
                    <p class="intro-box-en">{data['intro_en']}</p>
                    <p class="intro-box-zh">{data['intro_zh']}</p>
                </div>
                
                <h3 class="table-title">{data['table_title']}</h3>
                <table class="dest-table">
                    <thead>
                        <tr>
                            <th>City 城市</th>
                            <th>State 州</th>
                            <th>Highlights 特色</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="dest-city-cell">Brisbane<br>布里斯本</td>
                            <td>Queensland<br>昆士蘭州</td>
                            <td>Bridges, ferries, koalas, sand island<br>河流、橋梁、無尾熊、沙島</td>
                        </tr>
                        <tr>
                            <td class="dest-city-cell">Gold Coast<br>黃金海岸</td>
                            <td>Queensland<br>昆士蘭州</td>
                            <td>Beaches, theme parks, rainforest, glow-worms<br>沙灘、主題樂園、雨林、藍光蟲</td>
                        </tr>
                        <tr>
                            <td class="dest-city-cell">Sydney<br>雪梨</td>
                            <td>New South Wales<br>新南威爾斯州</td>
                            <td>Harbour, Opera House, sandstone buildings<br>港口、歌劇院、歷史建築、公園</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 2</span>
            </div>
        </div>
    """

    page_num = 3
    # Iterate through cities
    for city_idx, city in enumerate(data["cities"]):
        theme_class = "brisbane-theme" if city_idx == 0 else "goldcoast-theme" if city_idx == 1 else "sydney-theme"
        img_name = "brisbane.jpg" if city_idx == 0 else "gold_coast.jpg" if city_idx == 1 else "sydney.jpg"
        
        # Chapter Divider Page
        html += f"""
        <!-- PAGE {page_num}: CHAPTER DIVIDER - {city['name_en'].upper()} -->
        <div class="page chapter-divider {theme_class}">
            <div class="divider-title-group">
                <h2 class="divider-city-en">{city['name_en']}</h2>
                <h3 class="divider-city-zh">{city['name_zh']}</h3>
                <div class="divider-tagline">{city['tagline']}</div>
            </div>
            
            <div class="divider-desc-box">
                <p class="divider-desc-en">{city['desc_en']}</p>
                <p class="divider-desc-zh">{city['desc_zh']}</p>
            </div>
            
            <div class="divider-image-container">
                <img src="images/{img_name}" alt="{city['name_en']}" class="divider-image">
            </div>
            
            <div class="page-footer">
                <span>⭐ {city['name_en'].upper()}</span>
                <span>Page {page_num}</span>
            </div>
        </div>
        """
        page_num += 1
        
        # Attractions content
        attractions = city["attractions"]
        chunk_size = 3
        # If Sydney (index 2), last page has 4 items
        if city_idx == 2:
            chunks = [attractions[0:3], attractions[3:6], attractions[6:10]]
        else:
            chunks = [attractions[i:i + chunk_size] for i in range(0, len(attractions), chunk_size)]
            
        for chunk_idx, chunk in enumerate(chunks):
            list_class = "attractions-list four-items" if len(chunk) == 4 else "attractions-list"
            html += f"""
        <!-- PAGE {page_num}: {city['name_en'].upper()} ATTRACTIONS {chunk[0]['num']}-{chunk[-1]['num']} -->
        <div class="page {theme_class}">
            <div class="page-header">
                <span class="city-tag">{city['name_en'].upper()}</span>
                <span>EXPLORER GUIDE</span>
            </div>
            <div class="page-content">
                <div class="{list_class}">
            """
            
            for attr in chunk:
                html += f"""
                    <!-- Attraction Item {attr['num']} -->
                    <div class="attraction-item">
                        <h4 class="attraction-title">
                            <span class="number">{attr['num']}</span>
                            {attr['title']}
                        </h4>
                        <p class="attraction-desc-en">{attr['desc_en']}</p>
                        <p class="attraction-desc-zh">{attr['desc_zh']}</p>
                        
                        <div class="attraction-funfact">
                            <div class="funfact-title">💡 Fun Fact 趣味小知識</div>
                            <p class="funfact-text-en">{attr['fun_fact_en']}</p>
                            <p class="funfact-text-zh">{attr['fun_fact_zh']}</p>
                        </div>
                        <div class="attraction-source">{attr['source']}</div>
                    </div>
                """
                
            html += f"""
                </div>
            </div>
            <div class="page-footer">
                <span>⭐ {city['name_en'].upper()}</span>
                <span>Page {page_num}</span>
            </div>
        </div>
            """
            page_num += 1
            
    # Page 15: Challenges
    html += f"""
        <!-- PAGE 15: TRAVEL CHALLENGES -->
        <div class="page">
            <div class="page-header">
                <span>QUIZ TIME</span>
                <span>CHALLENGE</span>
            </div>
            <div class="page-content">
                <h3 class="challenge-title">Travel Challenge 旅行結束前的小挑戰</h3>
                <p class="challenge-intro">Let's see what you discovered! Can you answer these questions?</p>
                <div class="questions-container">
    """
    
    for idx, q in enumerate(data["challenges"]):
        html += f"""
                    <div class="question-card">
                        <span class="question-num">Q{idx+1}</span>
                        <p class="question-text-en">{q['en']}</p>
                        <p class="question-text-zh">{q['zh']}</p>
                        <div class="answer-line"></div>
                    </div>
        """
        
    html += """
                </div>
            </div>
            <div class="page-footer">
                <span>⭐ TRAVEL CHALLENGES</span>
                <span>Page 15</span>
            </div>
        </div>
    """
    
    # Page 16: Travel Diary & Back Cover
    html += """
        <!-- PAGE 16: DIARY & BACK COVER -->
        <div class="page back-cover">
            <div class="diary-section">
                <h3 class="diary-title">My Travel Notes 我的旅行日記</h3>
                <div class="writing-lines">
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                    <div class="writing-line"></div>
                </div>
            </div>
            <div class="back-closing">
                <div class="closing-banner">Have a wonderful trip!</div>
                <div class="closing-sub">祝你有一趟精彩的澳洲旅行！</div>
                <div class="stamp-decor">🐨 🦘 ✈️ 🗺️ 🏖️</div>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 16</span>
            </div>
        </div>
    """
    
    html += """
    </div>
</body>
</html>
"""
    
    with open('travel_book.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML booklet file generated successfully as travel_book.html")

if __name__ == '__main__':
    build_html()
