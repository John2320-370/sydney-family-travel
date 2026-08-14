# -*- coding: utf-8 -*-
import json

def build_html():
    with open('book_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    data["challenges"][0]["zh"] = "為什麼故事橋叫Story Bridge？"
    data["challenges"][0]["en"] = "Why is Story Bridge called Story Bridge?"
    
    # Precise image and photo credit mapping from Australia_2.docx + fallback IG photography
    attraction_media = {
        # Brisbane
        "1": {"img": "images/image1.jpg", "credit": "Photo: Brisbane City Council · CC BY 2.0 · Wikimedia Commons"},
        "2": {"img": "images/image2.jpg", "credit": "Photo: Cyron Ray Macey · CC BY 2.0 · Wikimedia Commons"},
        "3": {"img": "images/image3.jpg", "credit": "Photo: Fry72 · CC BY-SA 4.0 · Wikimedia Commons"},
        "4": {"img": "https://images.unsplash.com/photo-1510546020578-a35ad983d955?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "5": {"img": "https://images.unsplash.com/photo-1569003339405-ea396a5a8a90?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "6": {"img": "https://images.unsplash.com/photo-1601042879364-f3947d3f9c16?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "7": {"img": "images/image4.jpg", "credit": "Photo: Ishara Udawela · CC BY-SA 4.0 · Wikimedia Commons"},
        "8": {"img": "https://images.unsplash.com/photo-1611718037158-b118b6e2fe6e?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "9": {"img": "images/image5.jpg", "credit": "Photo: Kgbo · CC BY-SA 4.0 · Wikimedia Commons"},
        
        # Gold Coast
        "GC_1": {"img": "images/image6.jpg", "credit": "Photo: Anonymous · CC BY 4.0 · Wikimedia Commons"},
        "GC_2": {"img": "https://images.unsplash.com/photo-1612024782955-49fae79e42bb?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "GC_3": {"img": "https://images.unsplash.com/photo-1513889961551-628c1e5e2ee9?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "GC_4": {"img": "https://images.unsplash.com/photo-1570473541596-22418e61c3fd?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "GC_5": {"img": "images/image7.jpeg", "credit": "Photo: Harveychl · CC BY-SA 4.0 · Wikimedia Commons"},
        "GC_6": {"img": "images/image8.jpg", "credit": "Photo: Aliceinthealice · CC0 · Wikimedia Commons"},
        "GC_GW": {"img": "images/image9.jpg", "credit": "Photo: Yulanlu97 · CC BY-SA 4.0 · Wikimedia Commons"},
        
        # Sydney
        "SYD_1": {"img": "images/image10.jpg", "credit": "Photo: Roybb95 · CC BY-SA 3.0 · Wikimedia Commons"},
        "SYD_2": {"img": "images/image11.jpg", "credit": "Photo: Dietmar Rabich · CC BY-SA 4.0 · Wikimedia Commons"},
        "SYD_3": {"img": "https://images.unsplash.com/photo-1528072164453-f4e8ef9d475a?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "SYD_4": {"img": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "SYD_5": {"img": "images/image12.jpg", "credit": "Photo: Athena Lao · CC BY 2.0 · Wikimedia Commons"},
        "SYD_6": {"img": "https://images.unsplash.com/photo-1504509546545-e000b4a62425?auto=format&fit=crop&w=800&q=80", "credit": "Photo: Unsplash Photography"},
        "SYD_7": {"img": "images/image13.jpg", "credit": "Photo: JustARandomEditor123 · CC BY-SA 4.0 · Wikimedia Commons"},
        "SYD_8": {"img": "images/image14.jpg", "credit": "Photo: Dietmar Rabich · CC BY-SA 4.0 · Wikimedia Commons"},
        "SYD_9": {"img": "images/image15.jpg", "credit": "Photo: Dietmar Rabich · CC BY-SA 4.0 · Wikimedia Commons"},
        "SYD_10": {"img": "images/image16.jpg", "credit": "Photo: Toby Hudson · CC BY-SA 3.0 · Wikimedia Commons"}
    }

    html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Australia Travel Book - 我的澳洲旅行小書 (Australia_2 Edition)</title>
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
            --border-radius: 10px;
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
            padding: 14mm 15mm;
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
            font-size: 9.5pt;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 4px;
            z-index: 10;
        }

        .page-header span.city-tag {
            font-weight: bold;
        }

        .page-footer {
            font-family: 'Fredoka', sans-serif;
            font-size: 9.5pt;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 2px solid #f1f5f9;
            padding-top: 4px;
            z-index: 10;
        }

        .page-content {
            flex-grow: 1;
            padding: 5mm 0;
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
            margin-top: 5mm;
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
            margin-bottom: 12px;
        }

        .cover-cities {
            font-family: 'Fredoka', sans-serif;
            font-size: 15pt;
            color: var(--text-muted);
            letter-spacing: 1px;
            border-bottom: 2px solid #b45309;
            padding-bottom: 6px;
            margin-bottom: 10px;
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
            margin-bottom: 5mm;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .name-box {
            width: 100%;
            padding: 10px;
            border: 2px dashed #b45309;
            border-radius: 8px;
            font-size: 14pt;
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
            margin-top: 3mm;
        }

        .divider-city-en {
            font-family: 'Fredoka', sans-serif;
            font-size: 38pt;
            font-weight: 700;
            line-height: 1;
        }

        .divider-city-zh {
            font-size: 26pt;
            font-weight: 700;
            margin-top: 4px;
        }

        .divider-tagline {
            font-family: 'Fredoka', sans-serif;
            font-size: 11.5pt;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 10px;
            font-weight: 600;
        }

        .divider-desc-box {
            margin: 15px 0;
            padding: 15px;
            border-radius: var(--border-radius);
            font-size: 11.5pt;
            line-height: 1.55;
        }

        .divider-desc-en {
            font-weight: 500;
            margin-bottom: 8px;
            font-size: 12.5pt;
        }

        .divider-desc-zh {
            color: var(--text-muted);
            border-top: 1px dashed rgba(0,0,0,0.1);
            padding-top: 8px;
            font-size: 10.5pt;
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

        /* Theme Styling */
        .brisbane-theme { --theme-color: var(--brisbane-color); --theme-bg: var(--brisbane-bg); }
        .goldcoast-theme { --theme-color: var(--goldcoast-color); --theme-bg: var(--goldcoast-bg); }
        .sydney-theme { --theme-color: var(--sydney-color); --theme-bg: var(--sydney-bg); }

        .page.chapter-divider.brisbane-theme::before { border: 2px solid var(--brisbane-color); }
        .page.chapter-divider.goldcoast-theme::before { border: 2px solid var(--goldcoast-color); }
        .page.chapter-divider.sydney-theme::before { border: 2px solid var(--sydney-color); }

        .page.chapter-divider .divider-city-en { color: var(--theme-color); }
        .page.chapter-divider .divider-tagline { color: var(--text-muted); }
        .page.chapter-divider .divider-desc-box { background-color: var(--theme-bg); border-left: 5px solid var(--theme-color); }

        /* Attraction Item Styling - 2 Attractions per Page (Denser Layout) */
        .attractions-grid {
            display: flex;
            flex-direction: column;
            gap: 5mm;
            height: 100%;
            justify-content: space-between;
        }

        .attraction-card {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--border-radius);
            padding: 10px 12px;
            height: 48.5%;
        }

        .attraction-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1.5px solid var(--theme-color);
            padding-bottom: 3px;
            margin-bottom: 6px;
        }

        .attraction-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 16.5pt; /* Large font size maintained */
            font-weight: 700;
            color: var(--theme-color);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .attraction-title span.number {
            background-color: var(--theme-color);
            color: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11pt;
        }

        .attraction-body {
            display: flex;
            gap: 10px;
            align-items: flex-start;
            flex-grow: 1;
            margin-bottom: 6px;
        }

        .attraction-img-box {
            width: 42%;
            height: 52mm;
            border-radius: 6px;
            overflow: hidden;
            border: 2px solid #f1f5f9;
            flex-shrink: 0;
            position: relative;
        }

        .attraction-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .photo-credit {
            position: absolute;
            bottom: 2px;
            left: 2px;
            right: 2px;
            background: rgba(15, 23, 42, 0.75);
            color: #f8fafc;
            font-size: 6.5pt;
            padding: 2px 4px;
            border-radius: 3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .attraction-text-box {
            width: 58%;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        /* English Body Font Maintained Large: 16.5pt */
        .attraction-desc-en {
            font-size: 16.5pt;
            font-weight: 500;
            line-height: 1.35;
            color: var(--text-dark);
            text-align: justify;
        }

        .attraction-desc-zh {
            font-size: 9.5pt;
            line-height: 1.35;
            color: var(--text-muted);
            text-align: justify;
        }

        .attraction-funfact {
            background-color: var(--theme-bg);
            border: 1px dashed var(--theme-color);
            border-radius: 6px;
            padding: 6px 10px;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .funfact-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 9.5pt;
            font-weight: 700;
            color: var(--theme-color);
            display: flex;
            align-items: center;
            gap: 4px;
            text-transform: uppercase;
        }

        /* English Fun Fact Font Maintained Large: 14pt */
        .funfact-text-en {
            font-size: 14pt;
            font-weight: 600;
            color: #0f172a;
            line-height: 1.3;
        }

        .funfact-text-zh {
            font-size: 9.5pt;
            color: var(--text-muted);
            line-height: 1.3;
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
            margin-top: 5px;
        }

        .glowworm-label {
            font-family: 'Fredoka', sans-serif;
            font-size: 11pt;
            color: #38bdf8;
            letter-spacing: 2px;
            font-weight: 700;
            text-transform: uppercase;
        }

        .glowworm-title-en {
            font-family: 'Fredoka', sans-serif;
            font-size: 28pt;
            font-weight: 700;
            color: #ffffff;
            margin-top: 2px;
        }

        .glowworm-title-zh {
            font-size: 20pt;
            font-weight: 700;
            color: #38bdf8;
            margin-top: 2px;
        }

        .glowworm-main-layout {
            display: flex;
            gap: 15px;
            margin-top: 10px;
            align-items: stretch;
        }

        .glowworm-img-side {
            width: 40%;
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 2px solid #38bdf8;
            position: relative;
        }

        .glowworm-img-side img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .glowworm-info-side {
            width: 60%;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .glowworm-card {
            background-color: rgba(255,255,255,0.04);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 8px;
            padding: 10px 12px;
        }

        .glowworm-card-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 13pt;
            color: #38bdf8;
            font-weight: 700;
            margin-bottom: 4px;
            border-bottom: 1px solid rgba(56, 189, 248, 0.2);
            padding-bottom: 2px;
        }

        .glowworm-card-desc-en {
            font-size: 14pt;
            font-weight: 500;
            line-height: 1.4;
            color: #ffffff;
            margin-bottom: 4px;
        }

        .glowworm-card-desc-zh {
            font-size: 9.5pt;
            color: #94a3b8;
            line-height: 1.4;
        }

        .drawing-box-container {
            width: 100%;
            height: 60mm;
            border: 2px dashed #38bdf8;
            border-radius: var(--border-radius);
            background-color: rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #94a3b8;
            padding: 10px;
            margin-top: 10px;
        }

        .drawing-box-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 12pt;
            color: #38bdf8;
            font-weight: 700;
            margin-bottom: 3px;
        }

        .drawing-box-desc {
            font-size: 9.5pt;
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
            margin-top: 5mm;
            text-align: left;
        }

        .diary-title {
            font-family: 'Fredoka', sans-serif;
            font-size: 16pt;
            color: #0f766e;
            margin-bottom: 12px;
            border-bottom: 2px solid #99f6e4;
            padding-bottom: 4px;
        }

        .writing-lines {
            display: flex;
            flex-direction: column;
            gap: 18px;
            margin-top: 10px;
        }

        .writing-line {
            border-bottom: 1px dashed #cbd5e1;
            height: 25px;
        }

        .back-closing {
            margin-bottom: 8mm;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
        }

        .closing-banner {
            background-color: #0f766e;
            color: white;
            font-family: 'Fredoka', sans-serif;
            font-size: 15pt;
            font-weight: bold;
            padding: 8px 26px;
            border-radius: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .closing-sub {
            font-size: 12.5pt;
            font-weight: 700;
            color: #0f172a;
        }

        .stamp-decor {
            font-size: 22pt;
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
                padding: 14mm 15mm !important;
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
        <button class="btn-print" onclick="window.print()">🖨️ 列印旅遊手冊 (Print Booklet - 20 Pages)</button>
    </div>

    <div class="book-container">
"""
    
    # Total pages calculation:
    # 1: Cover
    # 2: Brisbane Divider
    # 3-7: Brisbane Attractions (9 items, 2 per page = 5 pages)
    # 8: Gold Coast Divider
    # 9-11: Gold Coast Attractions (6 items, 2 per page = 3 pages)
    # 12: Glow-worm Special Section (1 page)
    # 13: Sydney Divider
    # 14-18: Sydney Attractions (10 items, 2 per page = 5 pages)
    # 19: Travel Notes & Back Cover
    # Total = 19 -> let's make it 20 by adding an extra Travel Challenge/Note page or adjusting!
    # Let's count: 1 + 1 + 5 + 1 + 3 + 1 + 1 + 5 + 2 (Back cover + Quiz/Notes) = 20 pages! Perfect 20 pages!

    # Page 1: Cover Page
    html += """
        <!-- PAGE 1: COVER PAGE -->
        <div class="page cover-page">
            <div class="cover-header">
                <h1 class="cover-title">MY AUSTRALIA</h1>
                <h2 class="cover-subtitle">TRAVEL BOOK</h2>
                <div class="cover-cities">Brisbane &middot; Gold Coast &middot; Sydney</div>
                <p class="cover-desc">我的澳洲旅行小書 · 中英文旅遊小讀本 (Australia_2 Edition)</p>
            </div>
            <div class="cover-image-container">
                <img src="images/cover.jpg" alt="Australia Cover" class="cover-image">
            </div>
            <div class="cover-footer">
                <div class="name-box">Traveler 小小旅行家: _________________</div>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 1 of 20</span>
            </div>
        </div>
    """

    page_num = 2
    
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
                <span>Page {page_num} of 20</span>
            </div>
        </div>
        """
        page_num += 1
        
        attractions = city["attractions"]
        normal_attractions = []
        glowworm_attractions = []
        
        if city_idx == 1:
            for attr in attractions:
                if attr["num"] in ["7", "8", "9"]:
                    glowworm_attractions.append(attr)
                else:
                    normal_attractions.append(attr)
        else:
            normal_attractions = attractions
            
        # Group normal attractions 2 per page
        chunks = [normal_attractions[i:i + 2] for i in range(0, len(normal_attractions), 2)]
        
        for chunk in chunks:
            html += f"""
        <!-- PAGE {page_num}: {city['name_en'].upper()} ATTRACTIONS -->
        <div class="page {theme_class}">
            <div class="page-header">
                <span class="city-tag">{city['name_en'].upper()}</span>
                <span>EXPLORER GUIDE</span>
            </div>
            <div class="page-content">
                <div class="attractions-grid">
            """
            
            for attr in chunk:
                # Key lookup for media
                attr_num = attr["num"]
                key = attr_num
                if city_idx == 1:
                    key = f"GC_{attr_num}"
                elif city_idx == 2:
                    key = f"SYD_{attr_num}"
                    
                media = attraction_media.get(key, {"img": "images/cover.jpg", "credit": "Photo: Wikimedia Commons"})
                
                html += f"""
                    <!-- Attraction Card -->
                    <div class="attraction-card">
                        <div class="attraction-card-header">
                            <h4 class="attraction-title">
                                <span class="number">{attr['num']}</span>
                                {attr['title']}
                            </h4>
                        </div>
                        
                        <div class="attraction-body">
                            <div class="attraction-img-box">
                                <img src="{media['img']}" alt="{attr['title']}" class="attraction-img" loading="lazy">
                                <div class="photo-credit">{media['credit']}</div>
                            </div>
                            
                            <div class="attraction-text-box">
                                <p class="attraction-desc-en">{attr['desc_en']}</p>
                                <p class="attraction-desc-zh">{attr['desc_zh']}</p>
                            </div>
                        </div>
                        
                        <div class="attraction-funfact">
                            <div class="funfact-title">💡 Fun Fact 趣味小知識</div>
                            <p class="funfact-text-en">{attr['fun_fact_en']}</p>
                            <p class="funfact-text-zh">{attr['fun_fact_zh']}</p>
                        </div>
                    </div>
                """
                
            html += f"""
                </div>
            </div>
            <div class="page-footer">
                <span>⭐ {city['name_en'].upper()}</span>
                <span>Page {page_num} of 20</span>
            </div>
        </div>
            """
            page_num += 1
            
        # Render Glow-worm Special Section if city is Gold Coast (1 Compact Page)
        if city_idx == 1 and len(glowworm_attractions) > 0:
            gw_media = attraction_media.get("GC_GW", {"img": "images/image9.jpg", "credit": "Photo: Yulanlu97 · CC BY-SA 4.0"})
            html += f"""
        <!-- PAGE {page_num}: SPECIAL FEATURE - GLOW-WORMS -->
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
                
                <div class="glowworm-main-layout">
                    <div class="glowworm-img-side">
                        <img src="{gw_media['img']}" alt="Glow-worms">
                        <div class="photo-credit" style="bottom:4px;left:4px;right:4px;">{gw_media['credit']}</div>
                    </div>
                    
                    <div class="glowworm-info-side">
                        <div class="glowworm-card">
                            <h4 class="glowworm-card-title">💡 1. {glowworm_attractions[0]['title']}</h4>
                            <p class="glowworm-card-desc-en">{glowworm_attractions[0]['desc_en']}</p>
                            <p class="glowworm-card-desc-zh">{glowworm_attractions[0]['desc_zh']}</p>
                        </div>
                        
                        <div class="glowworm-card">
                            <h4 class="glowworm-card-title">💡 2. {glowworm_attractions[1]['title']}</h4>
                            <p class="glowworm-card-desc-en">{glowworm_attractions[1]['desc_en']}</p>
                            <p class="glowworm-card-desc-zh">{glowworm_attractions[1]['desc_zh']}</p>
                        </div>
                    </div>
                </div>
                
                <div class="glowworm-card" style="margin-top: 10px;">
                    <h4 class="glowworm-card-title">💡 3. {glowworm_attractions[2]['title']}</h4>
                    <p class="glowworm-card-desc-en">{glowworm_attractions[2]['desc_en']}</p>
                    <p class="glowworm-card-desc-zh">{glowworm_attractions[2]['desc_zh']}</p>
                </div>
                
                <div class="drawing-box-container">
                    <div class="drawing-box-title">🎨 Draw Your Own Glow-worm Cave! 畫出你的藍光蟲洞穴！</div>
                    <p class="drawing-box-desc">Use crayons to draw the dark cave and glowing blue stars! (畫出黑夜洞穴與點點藍光蟲)</p>
                </div>
            </div>
            
            <div class="page-footer" style="color: #94a3b8; border-top: 2px solid rgba(56, 189, 248, 0.2);">
                <span>⭐ GLOW-WORMS SPECIAL</span>
                <span>Page {page_num} of 20</span>
            </div>
        </div>
            """
            page_num += 1

    # Page 19: Travel Notes Page
    html += f"""
        <!-- PAGE 19: TRAVEL NOTES -->
        <div class="page">
            <div class="page-header">
                <span>MEMORIES</span>
                <span>TRAVEL SCRAPBOOK</span>
            </div>
            <div class="page-content">
                <div class="diary-section" style="margin-top:0;">
                    <h3 class="diary-title">My Favourite Moments 我的最愛時刻</h3>
                    <p style="font-size: 11pt; color: var(--text-muted); margin-bottom: 15px;">Draw or write about the best animal, beach, or building you saw in Australia!</p>
                    <div style="width: 100%; height: 160mm; border: 2px dashed #0f766e; border-radius: 10px; background: #f0fdfa; display: flex; justify-content: center; align-items: center; color: #0d9488; font-size: 12pt; font-weight: bold;">
                        🎨 Sticky Photo or Drawing Space (貼照片或畫畫區域)
                    </div>
                </div>
            </div>
            <div class="page-footer">
                <span>⭐ TRAVEL SCRAPBOOK</span>
                <span>Page 19 of 20</span>
            </div>
        </div>
    """

    # Page 20: Back Cover
    html += """
        <!-- PAGE 20: DIARY & BACK COVER -->
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
                </div>
            </div>
            <div class="back-closing">
                <div class="closing-banner">Have a wonderful trip!</div>
                <div class="closing-sub">祝你有一趟精彩的澳洲旅行！</div>
                <div class="stamp-decor">🐨 🦘 ✈️ 🛳️ 🏖️</div>
            </div>
            <div class="page-footer">
                <span>⭐ MY AUSTRALIA TRAVEL BOOK</span>
                <span>Page 20 of 20</span>
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
    print("HTML booklet rebuilt using Australia_2.docx images in a 20-page compact edition!")

if __name__ == '__main__':
    build_html()
