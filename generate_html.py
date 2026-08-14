# -*- coding: utf-8 -*-
import json

def build_html():
    with open('book_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Manual corrections for some fields
    data["challenges"][0]["zh"] = "為什麼故事橋叫Story Bridge？"
    data["challenges"][0]["en"] = "Why is Story Bridge called Story Bridge?"
    
    # Map of representative images from Unsplash for every single attraction
    unsplash_images = {
        # Brisbane
        "South Bank Parklands": "https://images.unsplash.com/photo-1590233649603-4e8c3b9b4d47?auto=format&fit=crop&w=800&q=80",
        "Story Bridge": "https://images.unsplash.com/photo-1549849171-09f62448c5dd?auto=format&fit=crop&w=800&q=80",
        "Lone Pine Koala Sanctuary": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=800&q=80",
        "Mount Coot-tha Lookout": "https://images.unsplash.com/photo-1510546020578-a35ad983d955?auto=format&fit=crop&w=800&q=80",
        "Queensland Museum": "https://images.unsplash.com/photo-1501290741922-b56c0d0974cf?auto=format&fit=crop&w=800&q=80",
        "Brisbane River and CityCat": "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=800&q=80",
        "Mulgumpin (Moreton Island)": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "Brisbane and Kaohsiung: Sister City": "https://images.unsplash.com/photo-1611718037158-b118b6e2fe6e?auto=format&fit=crop&w=800&q=80",
        "Brisbane and Kaohsiung: 姐妹市": "https://images.unsplash.com/photo-1611718037158-b118b6e2fe6e?auto=format&fit=crop&w=800&q=80",
        "Brisbane and Kaohsiung": "https://images.unsplash.com/photo-1611718037158-b118b6e2fe6e?auto=format&fit=crop&w=800&q=80",
        "The University of Queensland": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=800&q=80",
        
        # Gold Coast
        "Surfers Paradise": "https://images.unsplash.com/photo-1544913776-90c1223073a3?auto=format&fit=crop&w=800&q=80",
        "Currumbin Wildlife Sanctuary": "https://images.unsplash.com/photo-1612024782955-49fae79e42bb?auto=format&fit=crop&w=800&q=80",
        "Warner Bros. Movie World": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
        "Sea World": "https://images.unsplash.com/photo-1570473541596-22418e61c3fd?auto=format&fit=crop&w=800&q=80",
        "Q1大樓與SkyPoint觀景台": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80",
        "Springbrook and Natural Bridge": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=800&q=80",
        
        # Sydney
        "Sydney Opera House": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=800&q=80",
        "Sydney Harbour Bridge": "https://images.unsplash.com/photo-1524820197278-540916411e20?auto=format&fit=crop&w=800&q=80",
        "Circular Quay": "https://images.unsplash.com/photo-1549918830-11670403c488?auto=format&fit=crop&w=800&q=80",
        "Taronga Zoo": "https://images.unsplash.com/photo-1504618223053-559bdef9dd5a?auto=format&fit=crop&w=800&q=80",
        "Bondi Beach": "https://images.unsplash.com/photo-1518005020951-eccb494ad742?auto=format&fit=crop&w=800&q=80",
        "Darling Harbour": "https://images.unsplash.com/photo-1549637642-9018f0dbab12?auto=format&fit=crop&w=800&q=80",
        "Sydney Town Hall": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "Hyde Park": "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?auto=format&fit=crop&w=800&q=80",
        "聖母主教座堂 St Mary’s Cathedral": "https://images.unsplash.com/photo-1545638192-3a9ec2b10091?auto=format&fit=crop&w=800&q=80",
        "St Mary's Cathedral": "https://images.unsplash.com/photo-1545638192-3a9ec2b10091?auto=format&fit=crop&w=800&q=80",
        "The University of Sydney": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=800&q=80"
    }

    html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Australia Travel Book - 我的澳洲旅行小書</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Outfit:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f3f0ea;
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
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
            font-family: 'Fredoka', sans-serif;
        }

        .btn-print:hover {
            background-color: #047857;
            transform: translateY(-2px);
        }

        .book-container {
            display: flex;
            flex-direction: column;
            gap: 40px;
            align-items: center;
        }

        /* Page Layout - A4 Size */
        .page {
            width: 210mm;
            height: 297mm;
            background-color: var(--page-bg);
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            padding: 18mm 18mm;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            border-radius: 4px;
        }

        .page::before {
            content: '';
            position: absolute;
            top: 10mm;
            left: 10mm;
            right: 10mm;
            bottom: 10mm;
            border: 1px dashed #cbd5e1;
            pointer-events: none;
            border-radius: 8px;
            z-index: 1;
        }

        .page-header {
            font-family: 'Fredoka', sans-serif;
            font-size: 10pt;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 6px;
            z-index: 10;
        }

        .page-header span.city-tag {
            font-weight: bold;
        }

        .page-footer {
            font-family: 'Fredoka', sans-serif;
            font-size: 10pt;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 2px solid #f1f5f9;
            padding-top: 6px;
            z-index: 10;
        }

        .page-content {
            flex-grow: 1;
            padding: 8mm 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            z-index: 10;
            height: 100%;
        }

        /* Cover Page Styling */
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
            margin-top: 8mm;
        }

        .cover-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 38pt;
            font-weight: 700;
            color: #b45309;
            line-height: 1.1;
            margin-bottom: 5px;
        }

        .cover-subtitle {
            font-size: 26pt;
            font-weight: 700;
            color: #451a03;
            letter-spacing: 2px;
            margin-bottom: 15px;
        }

        .cover-cities {
            font-family: 'Fredoka', sans-serif;
            font-size: 16pt;
            color: var(--text-muted);
            letter-spacing: 1px;
            border-bottom: 2px solid #b45309;
            padding-bottom: 8px;
            margin-bottom: 12px;
            display: inline-block;
        }

        .cover-desc {
            font-size: 13pt;
            color: #78350f;
            font-weight: 500;
        }

        .cover-image-container {
            width: 100%;
            height: 110mm;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 6px solid white;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        }

        .cover-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .cover-footer {
            width: 85%;
            margin-bottom: 8mm;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .name-box {
            width: 100%;
            padding: 10px;
            border: 2px dashed #b45309;
            border-radius: 8px;
            font-size: 15pt;
            font-weight: bold;
            color: #451a03;
            background-color: rgba(255,255,255,0.6);
        }

        /* Chapter Divider Page */
        .page.chapter-divider {
            justify-content: space-between;
            padding: 18mm;
        }

        .divider-title-group {
            text-align: center;
            margin-top: 5mm;
        }

        .divider-city-en {
            font-family: 'Fredoka', sans-serif;
            font-size: 40pt;
            font-weight: 700;
            line-height: 1;
        }

        .divider-city-zh {
            font-size: 28pt;
            font-weight: 700;
            margin-top: 5px;
        }

        .divider-tagline {
            font-family: 'Fredoka', sans-serif;
            font-size: 12pt;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 12px;
            font-weight: 600;
        }

        .divider-desc-box {
            margin: 20px 0;
            padding: 18px;
            border-radius: var(--border-radius);
            font-size: 12pt;
            line-height: 1.6;
        }

        .divider-desc-en {
            font-weight: 500;
            margin-bottom: 10px;
            font-size: 13pt;
        }

        .divider-desc-zh {
            color: var(--text-muted);
            border-top: 1px dashed rgba(0,0,0,0.1);
            padding-top: 10px;
            font-size: 11pt;
        }

        .divider-image-container {
            width: 100%;
            height: 105mm;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 4px solid white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
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

        /* Attraction Item Styling - 1 Attraction per Page */
        .attraction-wrapper {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }

        .attraction-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 20pt;
            font-weight: 700;
            color: var(--theme-color);
            border-bottom: 2px solid var(--theme-color);
            padding-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
        }

        .attraction-title span.number {
            background-color: var(--theme-color);
            color: white;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14pt;
        }

        .attraction-img-container {
            width: 100%;
            height: 80mm;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 4px solid white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.06);
            margin-bottom: 10px;
        }

        .attraction-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* English font doubled in size as requested: ~18-20pt */
        .attraction-desc-en {
            font-size: 18.5pt;
            font-weight: 500;
            line-height: 1.5;
            color: var(--text-dark);
            text-align: justify;
            margin-bottom: 10px;
        }

        .attraction-desc-zh {
            font-size: 11pt;
            line-height: 1.5;
            color: var(--text-muted);
            text-align: justify;
            background-color: #f8fafc;
            border: 1px solid #f1f5f9;
            padding: 10px 15px;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .attraction-funfact {
            background-color: var(--theme-bg);
            border: 1.5px dashed var(--theme-color);
            border-radius: 8px;
            padding: 10px 14px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .funfact-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 11pt;
            font-weight: 700;
            color: var(--theme-color);
            display: flex;
            align-items: center;
            gap: 5px;
            text-transform: uppercase;
        }

        /* English font in fun fact doubled size: ~15pt */
        .funfact-text-en {
            font-size: 15pt;
            font-weight: 600;
            color: #0f172a;
            line-height: 1.4;
        }

        .funfact-text-zh {
            font-size: 10.5pt;
            color: var(--text-muted);
            line-height: 1.4;
        }

        .attraction-source {
            font-size: 8pt;
            color: var(--text-muted);
            text-align: right;
            font-style: italic;
            margin-top: 3px;
        }

        /* Glow-worm Special Section Styling */
        .glowworm-cover {
            background: linear-gradient(135deg, #090d16 0%, #152238 100%);
            color: #e2e8f0;
        }

        .glowworm-cover::before {
            border: 2px solid #38bdf8;
        }

        .glowworm-title-group {
            text-align: center;
            margin-top: 10px;
        }

        .glowworm-label {
            font-family: 'Fredoka', sans-serif;
            font-size: 12pt;
            color: #38bdf8;
            letter-spacing: 3px;
            font-weight: 700;
            text-transform: uppercase;
        }

        .glowworm-title-en {
            font-family: 'Fredoka', sans-serif;
            font-size: 32pt;
            font-weight: 700;
            color: #ffffff;
            margin-top: 5px;
        }

        .glowworm-title-zh {
            font-size: 22pt;
            font-weight: 700;
            color: #38bdf8;
            margin-top: 5px;
        }

        .glowworm-intro {
            font-size: 12pt;
            line-height: 1.6;
            margin: 15px 0;
            background-color: rgba(255,255,255,0.05);
            border-left: 4px solid #38bdf8;
            padding: 15px;
            border-radius: 4px;
            color: #f1f5f9;
        }

        .glowworm-card {
            background-color: rgba(255,255,255,0.03);
            border: 1px solid rgba(56, 189, 248, 0.2);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }

        .glowworm-card-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 14pt;
            color: #38bdf8;
            font-weight: 700;
            margin-bottom: 8px;
            border-bottom: 1px solid rgba(56, 189, 248, 0.2);
            padding-bottom: 3px;
        }

        .glowworm-card-desc-en {
            font-size: 14.5pt; /* Slightly smaller for fitting two on a page, but still very large */
            font-weight: 500;
            line-height: 1.5;
            color: #ffffff;
            margin-bottom: 8px;
        }

        .glowworm-card-desc-zh {
            font-size: 10.5pt;
            color: #94a3b8;
            line-height: 1.5;
        }

        /* Drawing Box for Glow-worms */
        .drawing-box-container {
            width: 100%;
            height: 90mm;
            border: 2px dashed #38bdf8;
            border-radius: var(--border-radius);
            background-color: rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #94a3b8;
            padding: 10px;
            margin-top: 15px;
        }

        .drawing-box-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 13pt;
            color: #38bdf8;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .drawing-box-desc {
            font-size: 10pt;
            text-align: center;
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
            margin-top: 8mm;
            text-align: left;
        }

        .diary-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 16pt;
            color: #0f766e;
            margin-bottom: 15px;
            border-bottom: 2px solid #99f6e4;
            padding-bottom: 5px;
        }

        .writing-lines {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-top: 15px;
        }

        .writing-line {
            border-bottom: 1px dashed #cbd5e1;
            height: 30px;
        }

        .back-closing {
            margin-bottom: 10mm;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }

        .closing-banner {
            background-color: #0f766e;
            color: white;
            font-family: 'Fredoka', sans-serif;
            font-size: 16pt;
            font-weight: bold;
            padding: 10px 30px;
            border-radius: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .closing-sub {
            font-size: 13pt;
            font-weight: 700;
            color: #0f172a;
        }

        .stamp-decor {
            font-size: 24pt;
            margin-top: 10px;
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
                <span>Page 1 of 32</span>
            </div>
        </div>
    """

    page_num = 2
    
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
                <span>Page {page_num} of 32</span>
            </div>
        </div>
        """
        page_num += 1
        
        # attractions processing
        attractions = city["attractions"]
        
        # If Gold Coast (index 1), split out Glow-worms (items 7, 8, 9) into the special segment
        normal_attractions = []
        glowworm_attractions = []
        
        if city_idx == 1:
            for attr in attractions:
                # Glow-worms are items 7, 8, 9
                if attr["num"] in ["7", "8", "9"]:
                    glowworm_attractions.append(attr)
                else:
                    normal_attractions.append(attr)
        else:
            normal_attractions = attractions
            
        # Render normal attractions (1 per page)
        for attr in normal_attractions:
            # Map Unsplash image
            attr_title_clean = attr["title"]
            # Find closest match in unsplash_images key
            img_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80" # fallback
            for k in unsplash_images.keys():
                if k in attr_title_clean or attr_title_clean in k:
                    img_url = unsplash_images[k]
                    break
                    
            html += f"""
        <!-- PAGE {page_num}: {city['name_en'].upper()} ATTRACTION - {attr['title']} -->
        <div class="page {theme_class}">
            <div class="page-header">
                <span class="city-tag">{city['name_en'].upper()}</span>
                <span>EXPLORER GUIDE</span>
            </div>
            <div class="page-content">
                <div class="attraction-wrapper">
                    <div>
                        <h4 class="attraction-title">
                            <span class="number">{attr['num']}</span>
                            {attr['title']}
                        </h4>
                        
                        <div class="attraction-img-container">
                            <img src="{img_url}" alt="{attr['title']}" class="attraction-img" loading="lazy">
                        </div>
                        
                        <p class="attraction-desc-en">{attr['desc_en']}</p>
                        <p class="attraction-desc-zh">{attr['desc_zh']}</p>
                    </div>
                    
                    <div>
                        <div class="attraction-funfact">
                            <div class="funfact-title">💡 Fun Fact 趣味小知識</div>
                            <p class="funfact-text-en">{attr['fun_fact_en']}</p>
                            <p class="funfact-text-zh">{attr['fun_fact_zh']}</p>
                        </div>
                        <div class="attraction-source">{attr['source']}</div>
                    </div>
                </div>
            </div>
            <div class="page-footer">
                <span>⭐ {city['name_en'].upper()}</span>
                <span>Page {page_num} of 32</span>
            </div>
        </div>
            """
            page_num += 1
            
        # Render Glow-worm Special Section if city is Gold Coast
        if city_idx == 1 and len(glowworm_attractions) > 0:
            # Glow-worms Part 1: Cover + Intro + What is + Why glow
            html += f"""
        <!-- PAGE {page_num}: SPECIAL FEATURE - GLOW-WORMS (PART 1) -->
        <div class="page glowworm-cover">
            <div class="page-header" style="color: #94a3b8; border-bottom: 2px solid rgba(56, 189, 248, 0.2);">
                <span>GOLD COAST SPECIAL</span>
                <span>BIOLUMINESCENCE EXPLORATION</span>
            </div>
            
            <div class="page-content" style="justify-content: flex-start;">
                <div class="glowworm-title-group">
                    <span class="glowworm-label">★ Special Feature ★</span>
                    <h2 class="glowworm-title-en">GLOW-WORMS</h2>
                    <h3 class="glowworm-title-zh">藍光蟲生態探秘</h3>
                </div>
                
                <div class="glowworm-intro">
                    In the quiet, dark, and wet caves of Springbrook rainforest, tiny living lights glow like blue-green stars in the dark. Let's learn about these magical creatures!
                </div>
                
                <!-- Glow-worm 1: Not a worm -->
                <div class="glowworm-card">
                    <h4 class="glowworm-card-title">💡 1. {glowworm_attractions[0]['title']}</h4>
                    <p class="glowworm-card-desc-en">{glowworm_attractions[0]['desc_en']}</p>
                    <p class="glowworm-card-desc-zh">{glowworm_attractions[0]['desc_zh']}</p>
                </div>
                
                <!-- Glow-worm 2: Why do they glow -->
                <div class="glowworm-card" style="margin-bottom: 0;">
                    <h4 class="glowworm-card-title">💡 2. {glowworm_attractions[1]['title']}</h4>
                    <p class="glowworm-card-desc-en">{glowworm_attractions[1]['desc_en']}</p>
                    <p class="glowworm-card-desc-zh">{glowworm_attractions[1]['desc_zh']}</p>
                </div>
            </div>
            
            <div class="page-footer" style="color: #94a3b8; border-top: 2px solid rgba(56, 189, 248, 0.2);">
                <span>⭐ GLOW-WORMS SPECIAL</span>
                <span>Page {page_num} of 32</span>
            </div>
        </div>
            """
            page_num += 1
            
            # Glow-worms Part 2: How to protect + Drawing activity
            html += f"""
        <!-- PAGE {page_num}: SPECIAL FEATURE - GLOW-WORMS (PART 2) -->
        <div class="page glowworm-cover">
            <div class="page-header" style="color: #94a3b8; border-bottom: 2px solid rgba(56, 189, 248, 0.2);">
                <span>GOLD COAST SPECIAL</span>
                <span>ECO CONSERVATION</span>
            </div>
            
            <div class="page-content" style="justify-content: flex-start;">
                <!-- Glow-worm 3: How to protect -->
                <div class="glowworm-card">
                    <h4 class="glowworm-card-title">💡 3. {glowworm_attractions[2]['title']}</h4>
                    <p class="glowworm-card-desc-en">{glowworm_attractions[2]['desc_en']}</p>
                    <p class="glowworm-card-desc-zh">{glowworm_attractions[2]['desc_zh']}</p>
                </div>
                
                <!-- Interactive Drawing Activity -->
                <div class="drawing-box-container">
                    <div class="drawing-box-title">🎨 Draw Your Own Glow-worm Cave!</div>
                    <div class="drawing-box-title" style="font-size: 11pt;">畫出你的藍光蟲洞穴！</div>
                    <p class="drawing-box-desc" style="margin-top: 8px;">Use crayons to draw the dark cave and add glowing blue stars using light blue or yellow! (可以畫出黑暗洞穴與點點藍光蟲！)</p>
                </div>
            </div>
            
            <div class="page-footer" style="color: #94a3b8; border-top: 2px solid rgba(56, 189, 248, 0.2);">
                <span>⭐ GLOW-WORMS SPECIAL</span>
                <span>Page {page_num} of 32</span>
            </div>
        </div>
            """
            page_num += 1

    # Page 32: Travel Diary & Back Cover
    html += f"""
        <!-- PAGE 32: DIARY & BACK COVER -->
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
                <div class="stamp-decor">🐨 🦘 ✈️ 運 🛳️ 🏖️</div>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 32 of 32</span>
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
    print("HTML booklet file generated successfully as travel_book.html with 32 pages.")

if __name__ == '__main__':
    build_html()
