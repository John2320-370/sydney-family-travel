/* =========================================================
   Sydney Explorer - Interactive Travel Planner JS Logic
   ========================================================= */

// --- 1. ITINERARY DATASET ---
const ITINERARY_DATA = {
  days: [
    {
      id: "day1",
      dayNum: 1,
      dateStr: "8/22",
      fullDate: "2026-08-22 (週五)",
      title: "初抵雪梨・海港之夜",
      area: "雪梨機場 ➔ 市區 ➔ 環形碼頭 ＆ 歌劇院",
      weather: {
        temp: "11°C - 19°C",
        condition: "晴時多雲",
        icon: "fa-cloud-sun",
        sunset: "17:33",
        uv: "3 (中等)",
        dressing: "傍晚海邊風大，建議薄長袖加穿防風保暖外套。"
      },
      spots: [
        {
          id: "d1-1",
          order: 1,
          name: "雪梨國際機場 (SYD T1)",
          type: "transport",
          typeName: "交通抵達",
          time: "14:00 - 15:30",
          duration: "1.5 小時",
          lat: -33.9399,
          lng: 151.1753,
          desc: "班機降落雪梨機場，領取行李並順利通關。",
          childFriendly: "在機場超商（WHSmith）或服務櫃檯順手為 7 歲小朋友領取免費「綠色 Child Opal 卡」並儲值。",
          warning: "建議直接叫 Uber / 計程車直達市區飯店（約 $55 AUD），避開 3 人拖大行李搭火車的折騰。",
          planB: "若班機延誤，直接前往飯店 Check-in 後直奔歌劇院晚餐。"
        },
        {
          id: "d1-2",
          order: 2,
          name: "市區飯店 Check-in（環形碼頭/溫亞德周邊）",
          type: "stay",
          typeName: "飯店休整",
          time: "16:00 - 17:00",
          duration: "1 小時",
          lat: -33.8634,
          lng: 151.2065,
          desc: "放妥行李、稍作梳洗，換上保暖輕便外套準備出發漫步。",
          childFriendly: "讓小朋友在房間喝水吃點心、休息 30 分鐘調整飛行時差體力。",
          warning: "市區停車費極貴，前兩天市區行程完全不需租車。",
          planB: "無"
        },
        {
          id: "d1-3",
          order: 3,
          name: "環形碼頭 ＆ 雪梨歌劇院夜景",
          type: "attraction",
          typeName: "核心景點",
          time: "17:30 - 19:15",
          duration: "1.75 小時",
          lat: -33.8568,
          lng: 151.2153,
          desc: "近距離欣賞世界遺產歌劇院的風帆建築與雪梨港灣大橋壯麗夕陽點燈。",
          childFriendly: "碼頭人行道寬敞平坦，看港灣來往雙層渡輪開過，小孩非常興奮。",
          warning: "冬末約 17:30 天黑，海港邊入夜體感僅約 10°C，務必為小孩戴上毛帽。",
          planB: "若下雨可走入歌劇院前廊遮雨迴廊，或前往市中心購物商場。"
        },
        {
          id: "d1-4",
          order: 4,
          name: "The Squires Landing 景觀晚餐",
          type: "food",
          typeName: "海港美食",
          time: "19:30 - 21:00",
          duration: "1.5 小時",
          lat: -33.8582,
          lng: 151.2097,
          desc: "坐落於當代藝術館旁，坐擁正面歌劇院無敵夜景，提供高品質澳洲牛排、漢堡與精釀飲品。",
          childFriendly: "氣氛輕鬆不拘謹，有專屬兒童漢堡與薯條菜單，適合剛抵達放鬆。",
          warning: "熱門海景座位建議提前 1-2 週線上預訂。",
          planB: "如客滿可改至旁邊的 Pancakes on The Rocks 享用美味肋排與鬆餅。"
        }
      ]
    },
    {
      id: "day2",
      dayNum: 2,
      dateStr: "8/23",
      fullDate: "2026-08-23 (週六)",
      title: "櫻花祭 ＆ 魔法城堡 ＆ 高空之巔",
      area: "西區奧本 ➔ 紐鎮 ➔ 雪梨大學 ➔ 雪梨塔",
      weather: {
        temp: "10°C - 18°C",
        condition: "微風晴朗",
        icon: "fa-sun",
        sunset: "17:34",
        uv: "4 (中等)",
        dressing: "白天戶外走動溫和，早晚日落後需保暖外套。"
      },
      spots: [
        {
          id: "d2-1",
          order: 1,
          name: "奧本植物園櫻花祭 (Auburn Cherry Blossom)",
          type: "attraction",
          typeName: "季節限定",
          time: "09:30 - 12:00",
          duration: "2.5 小時",
          lat: -33.8687,
          lng: 151.0321,
          desc: "南半球 8 月限定盛會！走訪日式花園、鳥居與盛開櫻花步道，體驗日本文化與美食市集。",
          childFriendly: "園區內有孔雀、澳洲袋鼠與袋熊區，綠草如茵非常適合小朋友探索散步。",
          warning: "門票必須提前於 Oztix 預訂「家庭票 $46.95 AUD」，現場完全不售票！週六搭火車至 Auburn 站轉乘免費接駁巴士。",
          planB: "若遇大雨可提早回市區改去維多利亞女王大廈 (QVB) 與室內博物館。"
        },
        {
          id: "d2-2",
          order: 2,
          name: "Newtown 特色午餐 ＆ 草莓西瓜蛋糕",
          type: "food",
          typeName: "人氣美食",
          time: "12:30 - 13:45",
          duration: "1.25 小時",
          lat: -33.8975,
          lng: 151.1795,
          desc: "回市區順路造訪文青街區，品嚐 Black Star Pastry 傳奇草莓西瓜蛋糕或 Pastizzi 酥皮小點。",
          childFriendly: "草莓西瓜蛋糕清甜不膩，小朋友一吃就愛上！",
          warning: "店內座位較少，外帶至旁邊公園野餐也是絕佳選擇。",
          planB: "亦可直接至雪梨大學周邊學生咖啡館用餐。"
        },
        {
          id: "d2-3",
          order: 3,
          name: "雪梨大學主樓 Quadrangle（哈利波特城堡）",
          type: "attraction",
          typeName: "經典地標",
          time: "14:00 - 15:30",
          duration: "1.5 小時",
          lat: -33.8886,
          lng: 151.1873,
          desc: "世界排名前列的百年歷史校園，新哥德式砂岩古堡建築宛如霍格華茲魔法學校。",
          childFriendly: "帶 7 歲小朋友拍「哈利波特魔法照」，中庭大草坪安全開闊可盡情奔跑。",
          warning: "參觀純戶外建築約 1 小時即可，避免停留太久讓小孩無聊。",
          planB: "若下雨可至校內的周澤榮博物館（Chau Chak Wing Museum）看埃及木乃伊與恐龍化石（免費入場，小孩超愛）。"
        },
        {
          id: "d2-4",
          order: 4,
          name: "雪梨塔眼觀景台 (Sydney Tower Eye)",
          type: "attraction",
          typeName: "高空全景",
          time: "16:30 - 18:00",
          duration: "1.5 小時",
          lat: -33.8705,
          lng: 151.2088,
          desc: "登上 250 公尺高空觀景台，360 度俯瞰雪梨海灣、太平洋與日落晚霞。",
          childFriendly: "附贈 4D 動感影院體驗（有風吹、泡泡與水霧效果），小孩體驗感十足。",
          warning: "【重要避坑】僅購買純觀景台門票，千萬不要吃 Skyfeast 自助餐（口味評價差、CP 值極低）。",
          planB: "若遇天候不佳濃霧，門票可改期至 Day 4 傍晚登頂。"
        },
        {
          id: "d2-5",
          order: 5,
          name: "Chat Thai 泰式精選晚餐",
          type: "food",
          typeName: "排隊名店",
          time: "18:30 - 20:00",
          duration: "1.5 小時",
          lat: -33.8789,
          lng: 151.2052,
          desc: "位於市中心超人氣泰式料理，沙嗲肉串、泰式炒河粉（Pad Thai）與芒果糯米飯風味絕佳。",
          childFriendly: "炒河粉與炸雞翅不辣且甜香，小朋友接受度極高。",
          warning: "熱門時段需排隊 15-20 分鐘，建議 18:15 前抵達候位。",
          planB: "亦可至 Westfield 頂樓美食街有多元各國料理快速用餐。"
        }
      ]
    },
    {
      id: "day3",
      dayNum: 3,
      dateStr: "8/24",
      fullDate: "2026-08-24 (週日)",
      title: "藍山世界遺產・傾斜列車冒險",
      area: "市區 ➔ 藍山 Scenic World ➔ 蘿拉小鎮 ➔ 三姊妹峰",
      weather: {
        temp: "5°C - 14°C",
        condition: "山區多雲偏冷",
        icon: "fa-mountain",
        sunset: "17:35",
        uv: "3 (中等)",
        dressing: "藍山海拔較高氣溫比市區低 5-7 度！厚保暖外套、手套、毛帽必備。"
      },
      spots: [
        {
          id: "d3-1",
          order: 1,
          name: "自駕啟程前往藍山 (市區出發)",
          type: "transport",
          typeName: "自駕出發",
          time: "08:30 - 10:00",
          duration: "1.5 小時",
          lat: -33.8688,
          lng: 151.2093,
          desc: "強烈建議當天市區取車自駕（車程 90 分鐘直達），車內放妥保暖裝備與點心。",
          childFriendly: "在 NSW 法律下 7 歲兒童可使用成人安全帶（建議加裝攜帶型增高墊），自駕免去火車轉公車在寒風中等待。",
          warning: "山路平坦好開，但請遵守澳洲右駕靠左行駛原則。",
          planB: "若不想自駕，可參加中文精品小團一日遊（含飯店接送）。"
        },
        {
          id: "d3-2",
          order: 2,
          name: "景觀世界三大纜車 (Scenic World)",
          type: "attraction",
          typeName: "冒險樂園",
          time: "10:00 - 13:00",
          duration: "3 小時",
          lat: -33.7289,
          lng: 150.3015,
          desc: "搭乘全球最陡 52 度傾斜鐵道火車（Railway）、270米高空透明玻璃底空中纜車（Skyway）與雨林索道（Cableway）。",
          childFriendly: "【7歲男童全行程最愛第一名！】像坐溫和版雲霄飛車，穿越山洞與雨林棧道，刺激好玩又安全。",
          warning: "提前線上預訂通票（Discovery Pass），現場直接掃碼省去排隊。",
          planB: "雨天纜車照常營運，車廂內有遮雨頂棚。"
        },
        {
          id: "d3-3",
          order: 3,
          name: "蘿拉小鎮午餐 (Leura Garage) ＆ 復古糖果屋",
          type: "food",
          typeName: "英倫小鎮",
          time: "13:15 - 14:45",
          duration: "1.5 小時",
          lat: -33.7088,
          lng: 150.3323,
          desc: "造訪充滿英式風情的蘿拉小鎮，在改建自舊車庫的獲獎名店 Leura Garage 享用美味比薩與烤雞。",
          childFriendly: "午餐後帶小朋友逛鎮上的「The Candy Store」百年糖果鋪，挑選澳洲手工糖果！",
          warning: "假日小鎮街邊停車需稍微繞一下找車位。",
          planB: "亦可至旁邊的 The Wayzgoose Diner 享用鬆餅漢堡。"
        },
        {
          id: "d3-4",
          order: 4,
          name: "回音谷遠眺三姊妹峰 (Echo Point & Three Sisters)",
          type: "attraction",
          typeName: "壯麗奇景",
          time: "15:00 - 16:15",
          duration: "1.25 小時",
          lat: -33.7321,
          lng: 150.3121,
          desc: "全藍山視野最開闊的觀景台，俯瞰傑米遜峽谷與原住民傳說中的三姊妹奇岩。",
          childFriendly: "觀景步道平緩平整，遊客中心有原住民文化藝術品展示。",
          warning: "下午山風強勁，請為小朋友拉緊外套拉鍊。",
          planB: "如遇大霧伸手不見五指，可轉往藍山文化中心室內展覽館。"
        },
        {
          id: "d3-5",
          order: 5,
          name: "自駕返回雪梨市區 ＆ 港灣悠閒晚餐",
          type: "transport",
          typeName: "自駕回程",
          time: "16:30 - 18:00",
          duration: "1.5 小時",
          lat: -33.8634,
          lng: 151.2065,
          desc: "趁天色剛暗順暢開回市區還車或停放，晚餐推薦在飯店周邊享用熱騰騰拉麵或義大利麵早早休息。",
          childFriendly: "小朋友在回程車上剛好可以睡覺補眠充電。",
          warning: "避開週日晚間進城車潮，16:30 前出發最順暢。",
          planB: "無"
        }
      ]
    },
    {
      id: "day4",
      dayNum: 4,
      dateStr: "8/25",
      fullDate: "2026-08-25 (週一)",
      title: "渡輪海灣 ＆ 塔龍加動物園 ＆ 水族世界",
      area: "環形碼頭 ➔ 塔龍加動物園 ➔ 達令港 SEA LIFE",
      weather: {
        temp: "11°C - 19°C",
        condition: "海港晴朗",
        icon: "fa-sun",
        sunset: "17:36",
        uv: "4 (中等)",
        dressing: "搭乘渡輪與戶外動物園走動舒適，必帶遮陽帽與薄外套。"
      },
      spots: [
        {
          id: "d4-1",
          order: 1,
          name: "環形碼頭搭乘 F2 景觀渡輪",
          type: "transport",
          typeName: "渡輪體驗",
          time: "09:00 - 09:30",
          duration: "0.5 小時",
          lat: -33.8614,
          lng: 151.2108,
          desc: "從 4 號碼頭搭乘渡輪橫越雪梨港（12分鐘），海面上近距離飽覽歌劇院與海港大橋視角。",
          childFriendly: "大人刷信用卡、7歲小孩刷 Child Opal 卡（半價只要 $3.56 AUD），小孩超喜歡坐船吹海風。",
          warning: "週一早晨班次頻繁，上船前可先在碼頭買杯外帶咖啡。",
          planB: "若風浪過大停駛可搭乘公車經大橋前往。"
        },
        {
          id: "d4-2",
          order: 2,
          name: "塔龍加動物園 (Taronga Zoo) 深度生態",
          type: "attraction",
          typeName: "明星景點",
          time: "09:30 - 14:00",
          duration: "4.5 小時",
          lat: -33.8434,
          lng: 151.2413,
          desc: "依山傍海的世界級動物園！長頸鹿背景就是歌劇院天際線，近距離看無尾熊、袋鼠、鴨嘴獸與飛禽表演。",
          childFriendly: "【強烈推薦！】有空中纜車（Sky Safari）、海獅表演與互動觸摸區，寓教於樂滿分。",
          warning: "園區為順坡地形，建議「搭纜車到山頂，一路順走下山」最省力不累！",
          planB: "若有預約到【Wildlife Retreat at Taronga】生態酒店，可於本日 14:00 辦理入住享受專屬飼養員導覽。"
        },
        {
          id: "d4-3",
          order: 3,
          name: "渡輪直達達令港 ＆ 港灣午茶",
          type: "transport",
          typeName: "港灣接駁",
          time: "14:30 - 15:15",
          duration: "0.75 小時",
          lat: -33.8749,
          lng: 151.2009,
          desc: "從動物園碼頭搭渡輪直達達令港，水上漫遊欣賞沿岸現代風光。",
          childFriendly: "在船上欣賞美麗港灣，省去市區陸路塞車轉乘之苦。",
          warning: "留意班次時刻表，建議 14:20 抵達碼頭候船。",
          planB: "無"
        },
        {
          id: "d4-4",
          order: 4,
          name: "雪梨 SEA LIFE 水族館 (Darling Harbour)",
          type: "attraction",
          typeName: "海底王國",
          time: "15:30 - 17:30",
          duration: "2 小時",
          lat: -33.8696,
          lng: 151.2023,
          desc: "探索澳洲最大水族館！觀賞世界僅存的罕見儒艮（海牛）、大堡礁鯊魚隧道，搭乘小充氣船看企鵝。",
          childFriendly: "【套票首選】買「水族館 + 雪梨塔」2合1套票最超值！搭企鵝探險船與穿過鯊魚肚子底下，7歲小孩眼睛發亮！",
          warning: "【避坑指南】不建議買 4 合 1 套票（蠟像館多為西方大人名人，小孩沒共鳴；野生動物世界與塔龍加重複）。",
          planB: "全室內場館，不受任何雨天影響。"
        },
        {
          id: "d4-5",
          order: 5,
          name: "Pancakes On The Rocks 歡樂晚餐",
          type: "food",
          typeName: "經典美味",
          time: "18:00 - 19:30",
          duration: "1.5 小時",
          lat: -33.8732,
          lng: 151.1995,
          desc: "達令港旁享譽數十年的名店，招牌炭烤牛肋排、香濃起司比薩與經典草莓巧克力鬆餅塔。",
          childFriendly: "份量豐盛、氣氛活潑，鬆餅是所有小朋友的最愛晚餐結尾！",
          warning: "肋排份量較大，兩大一小點一份大肋排加一份鬆餅即非常飽足。",
          planB: "若想吃海鮮亦可選達令港邊的 Nick's Seafood Restaurant。"
        }
      ]
    },
    {
      id: "day5",
      dayNum: 5,
      dateStr: "8/26",
      fullDate: "2026-08-26 (週二)",
      title: "海鮮盛宴 ＆ 冬季座頭鯨震撼 ＆ 啟程返台",
      area: "雪梨魚市場 ➔ 環形碼頭賞鯨 ➔ 岩石區 ➔ 機場",
      weather: {
        temp: "11°C - 20°C",
        condition: "海港晴朗・外海有浪",
        icon: "fa-water",
        sunset: "17:37",
        uv: "4 (中等)",
        dressing: "出海賞鯨外海海風強勁，必須著防風連帽外套與保暖衣物。"
      },
      spots: [
        {
          id: "d5-1",
          order: 1,
          name: "雪梨魚市場 (Sydney Fish Market) 海鮮早午餐",
          type: "food",
          typeName: "頂級海鮮",
          time: "09:30 - 11:30",
          duration: "2 小時",
          lat: -33.8727,
          lng: 151.1925,
          desc: "南半球最大漁產市場！品嚐新鮮生蠔、起司焗烤龍蝦、扇貝生魚片與金黃酥脆炸魚薯條。",
          childFriendly: "現炸的熱騰騰 Fish & Chips 和烤干貝小孩超愛吃，還能看巨大的深海帝王蟹與鮪魚切割展示。",
          warning: "戶外座位海鷗很多會搶食，強烈建議在室內座位區用餐最安心！",
          planB: "室內用餐區環境乾淨舒適，不受雨天影響。"
        },
        {
          id: "d5-2",
          order: 2,
          name: "環形碼頭冬季座頭鯨巡航 (Whale Watching)",
          type: "attraction",
          typeName: "自然奇蹟",
          time: "12:30 - 15:30",
          duration: "3 小時",
          lat: -33.8614,
          lng: 151.2108,
          desc: "【8 月雪梨最大亮點！】正值萬隻座頭鯨北遷繁殖的最高峰！95% 以上超高機率近距離目睹巨鯨躍出水面拍浪。",
          childFriendly: "一生難忘的海洋自然課！親眼看到比公車還大的鯨魚跳躍，震撼無比。",
          warning: "【必備預防】外海浪大，**登船前半小時務必讓全家（尤其小孩）服用兒童暈船藥**；挑選 Captain Cook / Fantasea 雙體大船更平穩！",
          planB: "若當日外海風浪超過安全標準停航，船公司會全額退費或改期，可轉往雪梨當代藝術館 (MCA) 或澳洲國家海事博物館（室內有真實潛水艇與驅逐艦可登艦探索）。"
        },
        {
          id: "d5-3",
          order: 3,
          name: "岩石區歷史街區 (The Rocks) 採買伴手禮",
          type: "attraction",
          typeName: "歷史街區",
          time: "16:00 - 18:00",
          duration: "2 小時",
          lat: -33.8596,
          lng: 151.2078,
          desc: "漫步在雪梨最古老的砂岩小巷，逛特色手工藝店、採買澳洲頂級夏威夷豆、羊毛脂護膚品與無尾熊玩偶。",
          childFriendly: "在老街買手工冰淇淋（Messina Gelato），小孩吃得開心大人悠閒逛街。",
          warning: "店家通常 17:30 - 18:00 打烊，採買請把握傍晚時間。",
          planB: "若下雨可轉往 George Street 上的室內購物中心採買。"
        },
        {
          id: "d5-4",
          order: 4,
          name: "Munich Brauhaus 歡樂告別晚餐",
          type: "food",
          typeName: "歡樂美食",
          time: "18:00 - 19:30",
          duration: "1.5 小時",
          lat: -33.8589,
          lng: 151.2081,
          desc: "位於岩石區充滿節慶歡樂氣氛的餐廳，酥脆德國豬腳、烤半雞與大份量薯條，為雪梨之旅畫下完美句點。",
          childFriendly: "現場有活潑巴伐利亞音樂表演與兒童專屬餐點，用餐氣氛熱絡不怕小孩吵鬧。",
          warning: "用餐完畢後回飯店提領行李，預計 20:00 叫 Uber 出發前往機場。",
          planB: "亦可選擇海關大樓旁義大利餐廳 Graze MCA。"
        },
        {
          id: "d5-5",
          order: 5,
          name: "雪梨機場 T1 國際航廈 (準備 23:00 班機)",
          type: "transport",
          typeName: "賦歸返台",
          time: "20:15 - 23:00",
          duration: "2.75 小時",
          lat: -33.9399,
          lng: 151.1753,
          desc: "搭乘 Uber 約 20-25 分鐘直達機場，辦理退稅手續（TRS）、行李託運與出境安檢，搭乘 23:00 班機滿載美好回憶返台。",
          childFriendly: "機場出境後有兒童遊戲區與免稅店，讓小朋友上機前消耗最後體力好在飛機上熟睡。",
          warning: "若有購買退稅物品，請先備好 TRS App QR Code 節省排隊時間。",
          planB: "無"
        }
      ]
    }
  ]
};

// --- 2. GLOBAL STATE & MAP INSTANCE ---
let map = null;
let currentDayIndex = 0;
let currentFilter = 'all';
let markersLayer = null;
let routeLinesLayer = null;
let foodLayer = null;
let tileLayerVoyager = null;
let tileLayerSatellite = null;
let activeTile = 'voyager';
let showFoodLayer = false;
let activeSidebarMode = 'timeline';

// --- 2.5 WEATHER API INTEGRATION ---
let apiWeatherData = null;

function updateWeatherDataFromApi() {
  const url = 'https://api.open-meteo.com/v1/forecast?latitude=-33.8688&longitude=151.2093&daily=weather_code,temperature_2m_max,temperature_2m_min,sunset,precipitation_probability_max&timezone=Australia%2FSydney&forecast_days=16';
  
  fetch(url)
    .then(res => res.json())
    .then(data => {
      if (data && data.daily) {
        apiWeatherData = data.daily;
        // Merge API data into ITINERARY_DATA.days
        ITINERARY_DATA.days.forEach(day => {
          const parts = day.dateStr.split('/');
          const month = parts[0].padStart(2, '0');
          const date = parts[1].padStart(2, '0');
          const targetDateStr = `2026-${month}-${date}`;
          
          const idx = apiWeatherData.time.indexOf(targetDateStr);
          if (idx !== -1) {
            const maxTemp = Math.round(apiWeatherData.temperature_2m_max[idx]);
            const minTemp = Math.round(apiWeatherData.temperature_2m_min[idx]);
            const code = apiWeatherData.weather_code[idx];
            const prob = apiWeatherData.precipitation_probability_max[idx];
            const rawSunset = apiWeatherData.sunset[idx];
            let sunsetStr = day.weather.sunset;
            if (rawSunset && rawSunset.includes('T')) {
              sunsetStr = rawSunset.split('T')[1];
            }
            
            day.weather.temp = `${minTemp}°C - ${maxTemp}°C`;
            const { condition, icon } = translateWeatherCode(code);
            day.weather.condition = `${condition} ｜ 降雨 ${prob}% ｜ 📶 Live`;
            day.weather.icon = icon;
            day.weather.sunset = sunsetStr;
          }
        });
        renderCurrentDay();
      }
    })
    .catch(err => console.log('Weather API offline, using fallback data.', err));
}

function translateWeatherCode(code) {
  if (code === 0) return { condition: "晴朗", icon: "fa-sun" };
  if (code >= 1 && code <= 3) return { condition: "晴時多雲", icon: "fa-cloud-sun" };
  if (code === 45 || code === 48) return { condition: "有霧", icon: "fa-smog" };
  if (code >= 51 && code <= 55) return { condition: "毛毛雨", icon: "fa-cloud-rain" };
  if (code >= 61 && code <= 65) return { condition: "下雨", icon: "fa-cloud-showers-heavy" };
  if (code >= 80 && code <= 82) return { condition: "局部陣雨", icon: "fa-cloud-sun-rain" };
  if (code >= 95) return { condition: "雷雨", icon: "fa-cloud-bolt" };
  return { condition: "多雲", icon: "fa-cloud" };
}

// --- 3. INITIALIZATION ---
document.addEventListener('DOMContentLoaded', () => {
  initMap();
  renderDayTabs();
  renderCurrentDay();
  initEventListeners();
  updateWeatherDataFromApi();
});

// --- 4. MAP INITIALIZATION ---
function initMap() {
  // Center on Sydney
  map = L.map('map', {
    zoomControl: false
  }).setView([-33.8688, 151.2093], 13);

  // Add zoom control at bottom right
  L.control.zoom({ position: 'bottomright' }).addTo(map);

  // CartoDB Voyager Tile Layer (Modern, crisp, colorful)
  tileLayerVoyager = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a>, &copy; OpenStreetMap',
    maxZoom: 19
  });

  // Esri World Imagery (Satellite)
  tileLayerSatellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: '&copy; Esri, Earthstar Geographics',
    maxZoom: 19
  });

  tileLayerVoyager.addTo(map);

  markersLayer = L.layerGroup().addTo(map);
  routeLinesLayer = L.layerGroup().addTo(map);
  foodLayer = L.layerGroup().addTo(map);
}

// --- 5. RENDER DAY TABS ---
function renderDayTabs() {
  const container = document.getElementById('day-tabs');
  container.innerHTML = '';

  ITINERARY_DATA.days.forEach((day, idx) => {
    const btn = document.createElement('button');
    btn.className = `day-tab-btn ${idx === currentDayIndex ? 'active' : ''}`;
    btn.innerHTML = `
      <span class="day-label">Day ${day.dayNum}</span>
      <span class="day-date">${day.dateStr}</span>
    `;
    btn.addEventListener('click', () => {
      if (currentDayIndex !== idx) {
        currentDayIndex = idx;
        document.querySelectorAll('.day-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderCurrentDay();
      }
    });
    container.appendChild(btn);
  });
}

// --- 6. RENDER CURRENT DAY ITINERARY ---
function renderCurrentDay() {
  const day = ITINERARY_DATA.days[currentDayIndex];
  
  // 1. Update Daily Weather & Overview Card
  const summaryCard = document.getElementById('daily-summary-card');
  summaryCard.innerHTML = `
    <div class="summary-top">
      <div class="theme-tag-wrap">
        <h3><i class="fa-solid fa-map-pin" style="color: #38bdf8;"></i> Day ${day.dayNum}：${day.title}</h3>
        <p class="theme-area"><i class="fa-solid fa-location-dot"></i> ${day.area}</p>
      </div>
      <div class="weather-widget">
        <i class="fa-solid ${day.weather.icon} weather-icon"></i>
        <div class="weather-info">
          <div class="temp">${day.weather.temp}</div>
          <div class="condition">${day.weather.condition} ｜ 日落 ${day.weather.sunset}</div>
        </div>
      </div>
    </div>
    <div class="daily-tips-bar">
      <i class="fa-solid fa-shirt" style="color: #f59e0b;"></i>
      <span><strong>穿搭與日照叮嚀：</strong>${day.weather.dressing}</span>
    </div>
  `;

  // 2. Filter Spots
  const filteredSpots = day.spots.filter(spot => {
    if (currentFilter === 'child') return spot.childFriendly && spot.childFriendly.length > 0;
    if (currentFilter === 'food') return spot.type === 'food';
    if (currentFilter === 'planb') return spot.planB && spot.planB !== '無';
    return true;
  });

  document.getElementById('current-day-title').innerText = `${day.fullDate} 行程清單`;
  document.getElementById('spots-count').innerText = `${filteredSpots.length} 個行程`;

  // 3. Render Timeline Cards
  const timelineList = document.getElementById('timeline-list');
  timelineList.innerHTML = '';

  let totalDistKm = 0;
  let totalMinutes = 0;

  filteredSpots.forEach((spot, idx) => {
    // Calculate distance & time to next spot
    let transitHtml = '';
    if (idx < filteredSpots.length - 1) {
      const nextSpot = filteredSpots[idx + 1];
      const dist = calculateDistance(spot.lat, spot.lng, nextSpot.lat, nextSpot.lng);
      totalDistKm += dist;
      
      const { mode, minutes } = estimateTransit(dist, spot.name, nextSpot.name);
      totalMinutes += minutes;

      transitHtml = `
        <div class="transit-step">
          <i class="${getTransitIcon(mode)}"></i>
          <span>至下個行程約 <strong>${dist.toFixed(1)} km</strong>（${mode}約 <strong>${minutes} 分鐘</strong>）</span>
        </div>
      `;
    }

    const item = document.createElement('div');
    item.className = 'timeline-item';
    item.id = `timeline-item-${spot.id}`;

    let childBoxHtml = '';
    if (spot.childFriendly) {
      childBoxHtml = `
        <div class="spot-child-box">
          <i class="fa-solid fa-child-reaching"></i>
          <div>
            <div class="child-title">🧒 7歲男童亮點評估：</div>
            <div class="child-content">${spot.childFriendly}</div>
          </div>
        </div>
      `;
    }

    let warningBoxHtml = '';
    if (spot.warning) {
      warningBoxHtml = `
        <div class="spot-warning-box">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <div>
            <div class="warning-content"><strong>⚠️ 避坑提醒：</strong>${spot.warning}</div>
          </div>
        </div>
      `;
    }

    let planBHtml = '';
    if (spot.planB && spot.planB !== '無') {
      planBHtml = `
        <div class="spot-planb-box">
          <i class="fa-solid fa-cloud-rain"></i>
          <div><strong>🌧️ 雨天備案 Plan B：</strong>${spot.planB}</div>
        </div>
      `;
    }

    const foodRegion = getFoodRegion(spot);
    let foodBtnHtml = '';
    if (foodRegion) {
      foodBtnHtml = `
        <button class="btn-food-trigger" onclick="event.stopPropagation(); showFoodRecommendations('${foodRegion}', '${spot.name}')">
          <i class="fa-solid fa-utensils"></i> 查看周邊美食 (5選)
        </button>
      `;
    }

    item.innerHTML = `
      <div class="timeline-node">${spot.order}</div>
      <div class="spot-card" onclick="focusSpot('${spot.id}', ${spot.lat}, ${spot.lng})">
        <div class="spot-header">
          <div class="spot-time-wrap">
            <span class="spot-time"><i class="fa-regular fa-clock"></i> ${spot.time}</span>
            <span class="spot-duration">停留約 ${spot.duration}</span>
          </div>
          <span class="spot-type-tag type-${spot.type}">${spot.typeName}</span>
        </div>
        <h4 class="spot-name">${spot.name}</h4>
        <p class="spot-desc">${spot.desc}</p>
        ${childBoxHtml}
        ${warningBoxHtml}
        ${planBHtml}
        ${foodBtnHtml}
      </div>
      ${transitHtml}
    `;

    timelineList.appendChild(item);
  });

  // 4. Update Route Summary Bar
  document.getElementById('total-distance').innerText = `${totalDistKm.toFixed(1)} km`;
  document.getElementById('total-transit-time').innerText = `${totalMinutes} 分鐘`;

  // 5. Update Map Markers & Polylines
  renderMapMarkersAndRoutes(day.spots);

  // 6. Update Food Sidebar & Map Layers
  renderFoodSidebar();
  renderFoodMarkers();
}

// --- 7. MAP MARKERS & ROUTE POLYLINES ---
function renderMapMarkersAndRoutes(spots) {
  markersLayer.clearLayers();
  routeLinesLayer.clearLayers();

  if (!spots || spots.length === 0) return;

  const latLngs = [];

  spots.forEach((spot) => {
    const latLng = [spot.lat, spot.lng];
    latLngs.push(latLng);

    // Custom HTML Pin Icon
    const customIcon = L.divIcon({
      className: 'custom-div-icon',
      html: `<div class="custom-map-pin" id="pin-${spot.id}"><span>${spot.order}</span></div>`,
      iconSize: [32, 32],
      iconAnchor: [16, 32],
      popupAnchor: [0, -32]
    });

    const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(spot.name)}&destination_place_id=${spot.lat},${spot.lng}`;

    const popupContent = `
      <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 220px; color: #0f172a; padding: 4px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
          <span style="font-size: 11px; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 2px 6px; border-radius: 4px;">${spot.time}</span>
          <span style="font-size: 11px; color: #64748b;">停留 ${spot.duration}</span>
        </div>
        <h4 style="margin: 4px 0 6px 0; font-size: 14px; font-weight: 700; color: #0f172a;">${spot.order}. ${spot.name}</h4>
        <p style="font-size: 12px; color: #475569; margin-bottom: 8px; line-height: 1.4;">${spot.desc}</p>
        <a href="${googleMapsUrl}" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; font-size: 11px; color: #0284c7; text-decoration: none; font-weight: 600;">
          <i class="fa-solid fa-arrow-up-right-from-square"></i> 在 Google Maps 中開啟導航
        </a>
      </div>
    `;

    const marker = L.marker(latLng, { icon: customIcon }).addTo(markersLayer);
    marker.bindPopup(popupContent);

    marker.on('click', () => {
      highlightActiveSpot(spot.id);
    });
  });

  // Draw smooth polyline for route
  if (latLngs.length > 1) {
    const polyline = L.polyline(latLngs, {
      color: '#0ea5e9',
      weight: 4,
      opacity: 0.8,
      dashArray: '8, 8',
      lineCap: 'round',
      lineJoin: 'round'
    }).addTo(routeLinesLayer);
  }

  // Fit bounds to show all spots
  if (latLngs.length > 0) {
    const bounds = L.latLngBounds(latLngs);
    map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
  }
}

// --- 8. FOCUS SPOT ON CLICK ---
window.focusSpot = function(spotId, lat, lng) {
  highlightActiveSpot(spotId);
  map.flyTo([lat, lng], 15, {
    animate: true,
    duration: 1.2
  });

  // Open corresponding marker popup
  markersLayer.eachLayer(layer => {
    if (layer.getLatLng && layer.getLatLng().lat === lat && layer.getLatLng().lng === lng) {
      layer.openPopup();
    }
  });

  // Show Quick View Card at bottom of map
  const day = ITINERARY_DATA.days[currentDayIndex];
  const spot = day.spots.find(s => s.id === spotId);
  if (spot) {
    showQuickCard(spot);
  }
};

function highlightActiveSpot(spotId) {
  // Highlight timeline item
  document.querySelectorAll('.timeline-item').forEach(el => el.classList.remove('active'));
  const activeItem = document.getElementById(`timeline-item-${spotId}`);
  if (activeItem) {
    activeItem.classList.add('active');
    activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Highlight map pin
  document.querySelectorAll('.custom-map-pin').forEach(pin => pin.classList.remove('active-pin'));
  const pin = document.getElementById(`pin-${spotId}`);
  if (pin) {
    pin.classList.add('active-pin');
  }
}

function showQuickCard(spot) {
  const card = document.getElementById('spot-quick-card');
  const body = document.getElementById('quick-card-content');
  const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(spot.name)}`;

  body.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
      <div>
        <span style="font-size: 11px; background: rgba(14, 165, 233, 0.2); color: #38bdf8; padding: 2px 8px; border-radius: 4px; font-weight: 700;">${spot.time} ｜ 建議停留 ${spot.duration}</span>
        <h3 style="font-size: 1.1rem; color: #fff; margin: 6px 0 4px 0;">${spot.order}. ${spot.name}</h3>
      </div>
      <a href="${googleMapsUrl}" target="_blank" class="btn btn-primary" style="font-size: 0.75rem; padding: 6px 12px;">
        <i class="fa-solid fa-location-arrow"></i> Google 導航
      </a>
    </div>
    <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 6px;">${spot.desc}</p>
  `;
  card.style.display = 'block';
}

// --- 9. DISTANCE & TRANSIT ESTIMATION HELPERS ---
function calculateDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // Earth radius in km
  const dLat = (lat2 - lat1) * (Math.PI / 180);
  const dLon = (lon2 - lon1) * (Math.PI / 180);
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

function estimateTransit(distKm, fromName, toName) {
  // If in Blue Mountains day (dist > 50km)
  if (distKm > 40) {
    return { mode: '自駕高速', minutes: Math.round(distKm * 1.3) };
  }
  if (fromName.includes('渡輪') || toName.includes('渡輪') || toName.includes('動物園') || toName.includes('達令港')) {
    return { mode: '景觀渡輪/水上接駁', minutes: Math.round(distKm * 3.5 + 5) };
  }
  if (distKm < 1.2) {
    return { mode: '步行散策', minutes: Math.round(distKm * 15) };
  }
  return { mode: '市區火車/Uber', minutes: Math.round(distKm * 3 + 8) };
}

function getTransitIcon(mode) {
  if (mode.includes('自駕')) return 'fa-solid fa-car';
  if (mode.includes('渡輪')) return 'fa-solid fa-ferry';
  if (mode.includes('步行')) return 'fa-solid fa-person-walking';
  return 'fa-solid fa-train-subway';
}

// --- 10. EVENT LISTENERS ---
function initEventListeners() {
  // Filter chips
  document.querySelectorAll('.filter-chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      currentFilter = chip.dataset.filter;
      renderCurrentDay();
    });
  });

  // Fit all view
  document.getElementById('btn-toggle-view').addEventListener('click', () => {
    const day = ITINERARY_DATA.days[currentDayIndex];
    const latLngs = day.spots.map(s => [s.lat, s.lng]);
    if (latLngs.length > 0) {
      map.fitBounds(L.latLngBounds(latLngs), { padding: [50, 50] });
    }
  });

  // Map Tile Switchers
  document.getElementById('btn-tile-voyager').addEventListener('click', () => {
    if (activeTile !== 'voyager') {
      map.removeLayer(tileLayerSatellite);
      tileLayerVoyager.addTo(map);
      activeTile = 'voyager';
      document.getElementById('btn-tile-voyager').classList.add('active');
      document.getElementById('btn-tile-satellite').classList.remove('active');
    }
  });

  document.getElementById('btn-tile-satellite').addEventListener('click', () => {
    if (activeTile !== 'satellite') {
      map.removeLayer(tileLayerVoyager);
      tileLayerSatellite.addTo(map);
      activeTile = 'satellite';
      document.getElementById('btn-tile-satellite').classList.add('active');
      document.getElementById('btn-tile-voyager').classList.remove('active');
    }
  });

  // Close Quick Card
  document.getElementById('close-quick-card').addEventListener('click', () => {
    document.getElementById('spot-quick-card').style.display = 'none';
  });

  // Opal & Tools Modal
  const modal = document.getElementById('tools-modal');
  document.getElementById('btn-open-tools').addEventListener('click', () => {
    modal.style.display = 'flex';
  });

  document.getElementById('btn-close-modal').addEventListener('click', () => {
    modal.style.display = 'none';
  });

  // QR Code Modal
  const qrModal = document.getElementById('qrcode-modal');
  const btnShowQr = document.getElementById('btn-show-qrcode');
  if (btnShowQr) {
    btnShowQr.addEventListener('click', () => {
      qrModal.style.display = 'flex';
    });
  }

  const btnCloseQr = document.getElementById('btn-close-qrcode');
  if (btnCloseQr) {
    btnCloseQr.addEventListener('click', () => {
      qrModal.style.display = 'none';
    });
  }

  qrModal.addEventListener('click', (e) => {
    if (e.target === qrModal) {
      qrModal.style.display = 'none';
    }
  });

  // Food Modal
  const foodModal = document.getElementById('food-modal');
  const btnCloseFood = document.getElementById('btn-close-food');
  if (btnCloseFood) {
    btnCloseFood.addEventListener('click', () => {
      foodModal.style.display = 'none';
    });
  }

  foodModal.addEventListener('click', (e) => {
    if (e.target === foodModal) {
      foodModal.style.display = 'none';
    }
  });

  // Sidebar Mode Switcher (Timeline vs Food)
  const btnModeTimeline = document.getElementById('btn-mode-timeline');
  const btnModeFood = document.getElementById('btn-mode-food');
  const timelineWrap = document.getElementById('timeline-container-wrap');
  const foodWrap = document.getElementById('food-container-wrap');

  if (btnModeTimeline && btnModeFood) {
    btnModeTimeline.addEventListener('click', () => {
      activeSidebarMode = 'timeline';
      btnModeTimeline.classList.add('active');
      btnModeFood.classList.remove('active');
      timelineWrap.style.display = 'block';
      foodWrap.style.display = 'none';
      renderFoodMarkers();
    });

    btnModeFood.addEventListener('click', () => {
      activeSidebarMode = 'food';
      btnModeFood.classList.add('active');
      btnModeTimeline.classList.remove('active');
      timelineWrap.style.display = 'none';
      foodWrap.style.display = 'block';
      renderFoodMarkers();
    });
  }

  // Map Food Layer Toggle Button
  const btnToggleFoodLayer = document.getElementById('btn-toggle-food-layer');
  if (btnToggleFoodLayer) {
    btnToggleFoodLayer.addEventListener('click', () => {
      showFoodLayer = !showFoodLayer;
      if (showFoodLayer) {
        btnToggleFoodLayer.classList.add('active');
      } else {
        btnToggleFoodLayer.classList.remove('active');
      }
      renderFoodMarkers();
    });
  }
}

// --- 11. FOOD RECOMMENDATIONS LOGIC & DATABASE ---
function getFoodRegion(spot) {
  if (spot.id.startsWith('d1-2') || spot.id.startsWith('d1-3') || spot.id.startsWith('d1-4') || spot.id.startsWith('d3-5') || spot.id.startsWith('d4-1') || spot.id.startsWith('d4-2') || spot.id.startsWith('d5-2') || spot.id.startsWith('d5-3') || spot.id.startsWith('d5-4')) {
    return 'Circular Quay';
  }
  if (spot.id.startsWith('d2-1')) {
    return 'Auburn';
  }
  if (spot.id.startsWith('d2-2') || spot.id.startsWith('d2-3')) {
    return 'Newtown';
  }
  if (spot.id.startsWith('d2-4') || spot.id.startsWith('d2-5')) {
    return 'Sydney CBD';
  }
  if (spot.id.startsWith('d3-2') || spot.id.startsWith('d3-3') || spot.id.startsWith('d3-4')) {
    return 'Blue Mountains';
  }
  if (spot.id.startsWith('d4-3') || spot.id.startsWith('d4-4') || spot.id.startsWith('d4-5')) {
    return 'Darling Harbour';
  }
  if (spot.id.startsWith('d5-1')) {
    return 'Sydney Fish Market';
  }
  return null;
}

function showFoodRecommendations(region, spotName) {
  const modal = document.getElementById('food-modal');
  const title = document.getElementById('food-modal-title');
  const body = document.getElementById('food-modal-body');

  title.innerText = `${spotName} 周邊精選美食 (4.0★+)`;
  body.innerHTML = '';

  const restaurants = FOOD_RECOMMENDATIONS_DATABASE[region];
  if (!restaurants || restaurants.length === 0) {
    body.innerHTML = '<p style="color: var(--text-muted); text-align: center;">暫無此區域的美食推薦。</p>';
  } else {
    restaurants.forEach(rest => {
      const card = document.createElement('div');
      card.className = 'food-card';
      card.innerHTML = `
        <div class="food-card-header">
          <h4 class="food-card-title">${rest.name}</h4>
          <span class="food-card-rating"><i class="fa-solid fa-star"></i> ${rest.rating} ★</span>
        </div>
        <div class="food-card-meta">
          <span><i class="fa-solid fa-dollar-sign"></i> 價位: ${rest.price}</span>
          <span><i class="fa-solid fa-comments"></i> 評論數: ${rest.reviews}</span>
        </div>
        <p class="food-card-desc">${rest.desc}</p>
        <div class="food-card-child">
          <div class="child-title"><i class="fa-solid fa-child-reaching"></i> 🧒 7歲兒童點評：</div>
          <div class="child-content">${rest.childFriendly}</div>
        </div>
        <div class="food-card-footer">
          <a href="${rest.mapsUrl}" target="_blank" class="btn btn-outline" style="font-size: 0.72rem; padding: 4px 10px;">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> 在 Google Maps 中查看
          </a>
        </div>
      `;
      body.appendChild(card);
    });
  }

  modal.style.display = 'flex';
}

function renderFoodSidebar() {
  const listContainer = document.getElementById('food-list-sidebar');
  const foodCountBadge = document.getElementById('food-count');
  if (!listContainer) return;
  listContainer.innerHTML = '';

  const day = ITINERARY_DATA.days[currentDayIndex];
  const uniqueRegions = new Set();
  day.spots.forEach(spot => {
    const reg = getFoodRegion(spot);
    if (reg) uniqueRegions.add(reg);
  });

  let totalFoodCount = 0;
  uniqueRegions.forEach(region => {
    const restaurants = FOOD_RECOMMENDATIONS_DATABASE[region];
    if (restaurants) {
      totalFoodCount += restaurants.length;
      restaurants.forEach(rest => {
        const card = document.createElement('div');
        card.className = 'food-card';
        card.style.cursor = 'pointer';
        card.innerHTML = `
          <div class="food-card-header">
            <h4 class="food-card-title">${rest.name}</h4>
            <span class="food-card-rating"><i class="fa-solid fa-star"></i> ${rest.rating} ★</span>
          </div>
          <div class="food-card-meta">
            <span><i class="fa-solid fa-location-dot"></i> 區域: ${region}</span>
            <span><i class="fa-solid fa-dollar-sign"></i> 價位: ${rest.price}</span>
          </div>
          <p class="food-card-desc" style="font-size: 0.8rem; margin: 4px 0; color: #cbd5e1;">${rest.desc}</p>
          <div class="food-card-child" style="margin-top: 4px;">
            <span style="font-size: 0.72rem; color: #34d399; font-weight: 700;"><i class="fa-solid fa-child-reaching"></i> 兒童點評：</span>
            <span style="font-size: 0.72rem; color: #a7f3d0;">${rest.childFriendly}</span>
          </div>
          <div class="food-card-footer">
            <span style="font-size: 0.72rem; color: #38bdf8; font-weight: 600;"><i class="fa-solid fa-location-crosshairs"></i> 點擊地圖定位</span>
          </div>
        `;
        card.addEventListener('click', () => {
          focusFoodOnMap(rest.name, rest.lat, rest.lng, rest.desc);
        });
        listContainer.appendChild(card);
      });
    }
  });
  foodCountBadge.innerText = `${totalFoodCount} 家餐廳`;
}

function focusFoodOnMap(name, lat, lng, desc) {
  // Open food layer automatically if it was hidden
  if (!showFoodLayer) {
    showFoodLayer = true;
    const btn = document.getElementById('btn-toggle-food-layer');
    if (btn) btn.classList.add('active');
  }
  renderFoodMarkers();

  map.flyTo([lat, lng], 15, {
    animate: true,
    duration: 1.2
  });

  // Highlight the active pin
  document.querySelectorAll('.custom-food-pin').forEach(pin => pin.classList.remove('active-food-pin'));
  const targetPin = document.getElementById(`food-pin-${name.replace(/\s+/g, '-')}`);
  if (targetPin) targetPin.classList.add('active-food-pin');

  // Open popup
  foodLayer.eachLayer(layer => {
    if (layer.getLatLng && layer.getLatLng().lat === lat && layer.getLatLng().lng === lng) {
      layer.openPopup();
    }
  });
}

function renderFoodMarkers() {
  foodLayer.clearLayers();
  
  // Show if toggled ON or if viewing the food list sidebar tab
  const activeShow = showFoodLayer || (activeSidebarMode === 'food');
  
  if (!activeShow) return;

  const day = ITINERARY_DATA.days[currentDayIndex];
  const uniqueRegions = new Set();
  day.spots.forEach(spot => {
    const reg = getFoodRegion(spot);
    if (reg) uniqueRegions.add(reg);
  });

  uniqueRegions.forEach(region => {
    const restaurants = FOOD_RECOMMENDATIONS_DATABASE[region];
    if (restaurants) {
      restaurants.forEach(rest => {
        const latLng = [rest.lat, rest.lng];

        // Custom Food icon marker
        const customIcon = L.divIcon({
          className: 'custom-food-div-icon',
          html: `<div class="custom-food-pin" id="food-pin-${rest.name.replace(/\s+/g, '-')}"><i class="fa-solid fa-utensils"></i></div>`,
          iconSize: [28, 28],
          iconAnchor: [14, 28],
          popupAnchor: [0, -28]
        });

        const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(rest.name)}&destination_place_id=${rest.lat},${rest.lng}`;

        const popupContent = `
          <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 200px; color: #0f172a; padding: 4px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
              <span style="font-size: 10px; font-weight: 700; color: #ea580c; background: #ffedd5; padding: 2px 6px; border-radius: 4px;">今日推薦美食</span>
              <span style="font-size: 11px; color: #fbbf24; font-weight: 700;"><i class="fa-solid fa-star"></i> ${rest.rating}</span>
            </div>
            <h4 style="margin: 4px 0 6px 0; font-size: 14px; font-weight: 700; color: #0f172a;">${rest.name}</h4>
            <p style="font-size: 12px; color: #475569; margin-bottom: 8px; line-height: 1.4;">${rest.desc}</p>
            <a href="${googleMapsUrl}" target="_blank" style="display: inline-flex; align-items: center; gap: 4px; font-size: 11px; color: #ea580c; text-decoration: none; font-weight: 600;">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> 在 Google Maps 中開啟導航
            </a>
          </div>
        `;

        const marker = L.marker(latLng, { icon: customIcon }).addTo(foodLayer);
        marker.bindPopup(popupContent);
      });
    }
  });
}

const FOOD_RECOMMENDATIONS_DATABASE = {
  "Circular Quay": [
    {
      name: "Bennelong",
      rating: "4.5",
      reviews: "1,500+",
      price: "高檔",
      lat: -33.8568,
      lng: 151.2153,
      desc: "座落於雪梨歌劇院風帆內建築，提供頂級精緻現代澳洲料理，可飽覽港灣夜景。",
      childFriendly: "推薦預約中庭 Cured & Cultured 吧台區，氣氛較為輕鬆，可點選特製歌劇院外型 Pavlova 蛋白霜甜點，小孩超愛！",
      mapsUrl: "https://maps.google.com/?q=Bennelong+Sydney"
    },
    {
      name: "Cafe Sydney",
      rating: "4.5",
      reviews: "3,200+",
      price: "中高",
      lat: -33.8619,
      lng: 151.2109,
      desc: "海關大樓頂樓，擁有觀賞港灣大橋的絕佳景觀，主打海鮮與現代澳洲菜。",
      childFriendly: "露台區座位氣氛熱絡，服務人員對親子極度客氣，並備有精緻兒童餐點選項。",
      mapsUrl: "https://maps.google.com/?q=Cafe+Sydney"
    },
    {
      name: "The Meat & Wine Co (Circular Quay)",
      rating: "4.4",
      reviews: "1,200+",
      price: "中等",
      lat: -33.8582,
      lng: 151.2098,
      desc: "澳洲知名牛排連鎖，以其優質的和牛牛排（Wagyu Steaks）與獨門特調烤肉醬汁在社群上極具人氣。",
      childFriendly: "有專屬 Kid's Menu（含炸魚塊、小漢堡、冰淇淋與著色紙），環境非常親子友善。",
      mapsUrl: "https://maps.google.com/?q=The+Meat+&amp;+Wine+Co+Circular+Quay"
    },
    {
      name: "Opera Bar",
      rating: "4.3",
      reviews: "8,500+",
      price: "中等",
      lat: -33.8567,
      lng: 151.2145,
      desc: "歌劇院前廣場露天酒吧餐飲，擁有無敵雪梨大橋景色，下午時分非常熱鬧。",
      childFriendly: "全戶外空間完全不怕小孩吵鬧，炸魚薯條 (Fish & Chips) 與瑪格麗特披薩品質優秀，小孩超愛。",
      mapsUrl: "https://maps.google.com/?q=Opera+Bar"
    },
    {
      name: "Yayoi Garden (彌生軒旗艦店)",
      rating: "4.4",
      reviews: "1,000+",
      price: "中等",
      lat: -33.8637,
      lng: 151.2102,
      desc: "提供精緻日式定食，米飯香 Q、主菜入味，是市中心想吃熱騰騰亞洲飯食的救星。",
      childFriendly: "日式定食包含白飯、味噌湯與日式炸雞唐揚，符合亞洲小孩胃口，用餐環境乾淨且安靜。",
      mapsUrl: "https://maps.google.com/?q=Yayoi+Garden+Sydney"
    }
  ],
  "Auburn": [
    {
      name: "Darband Persian Restaurant",
      rating: "4.4",
      reviews: "1,250+",
      price: "實惠",
      lat: -33.8702,
      lng: 151.0325,
      desc: "奧本名氣最盛的波斯烤肉店，炭火現烤肉串香氣撲鼻，價格實惠。",
      childFriendly: "氣氛輕鬆溫馨，提供大盤肉排抓飯，番紅花開心果冰淇淋是小孩的甜點首選。",
      mapsUrl: "https://maps.google.com/?q=Darband+Persian+Restaurant+Auburn"
    },
    {
      name: "Tarim Uyghur Handmade Noodles",
      rating: "4.5",
      reviews: "650+",
      price: "中等偏低",
      lat: -33.8715,
      lng: 151.0318,
      desc: "主打純手工現拉麵條與傳統新疆維吾爾風味羊肉串和大盤雞。",
      childFriendly: "手工拉麵口感無敵，可要求做無辣的羊肉炒麵或丁丁炒麵，小孩非常喜歡。",
      mapsUrl: "https://maps.google.com/?q=Tarim+Uyghur+Handmade+Noodles+Auburn"
    },
    {
      name: "New Star Kebabs",
      rating: "4.2",
      reviews: "2,600+",
      price: "實惠",
      lat: -33.8706,
      lng: 151.0329,
      desc: "奧本地標級土耳其烤肉 institution，炭火旋轉烤肉拼盤與烤餅份量極大。",
      childFriendly: "土耳其肉片薯條盒（HSP）有滿滿起司與薯條，對小孩吸引力巨大。",
      mapsUrl: "https://maps.google.com/?q=New+Star+Kebabs+Auburn"
    },
    {
      name: "Dervish Turkish Restaurant",
      rating: "4.3",
      reviews: "520+",
      price: "中等偏低",
      lat: -33.8698,
      lng: 151.0331,
      desc: "提供精緻的土耳其船型起司烤餅（Pide）與豐富的烤肉家庭分享拼盤。",
      childFriendly: "店內寬敞明亮，船型起司烤餅不辣且奶香濃郁，是小孩極佳的午餐。",
      mapsUrl: "https://maps.google.com/?q=Dervish+Turkish+Restaurant+Auburn"
    },
    {
      name: "Gaziantep Sweets",
      rating: "4.6",
      reviews: "750+",
      price: "實惠",
      lat: -33.8709,
      lng: 151.0324,
      desc: "土耳其傳統甜點專賣店，提供現做的果仁蜜餅（Baklava）與會拉絲的熱起司 Knafeh。",
      childFriendly: "甜點天堂！搭配經典的土耳其羊奶冰淇淋，好玩又美味，極受小孩歡迎。",
      mapsUrl: "https://maps.google.com/?q=Gaziantep+Sweets+Auburn"
    }
  ],
  "Newtown": [
    {
      name: "Rising Sun Workshop",
      rating: "4.5",
      reviews: "920+",
      price: "中等",
      lat: -33.8996,
      lng: 151.1764,
      desc: "雪梨文青必朝聖的重機修車廠二樓拉麵店，概念新穎，拉麵水準極高。",
      childFriendly: "7歲男童最愛！一樓展示許多大重機與工具，吃拉麵同時可以大飽眼福。",
      mapsUrl: "https://maps.google.com/?q=Rising+Sun+Workshop+Newtown"
    },
    {
      name: "Cairo Takeaway",
      rating: "4.5",
      reviews: "1,050+",
      price: "中等偏低",
      lat: -33.8967,
      lng: 151.1798,
      desc: "提供美味的埃及街頭小吃，以現炸脆口鷹嘴豆泥丸（Falafel）與烤肉盤聞名。",
      childFriendly: "薯條與香脆丸子是經典手抓食物，適合小朋友隨性享用。",
      mapsUrl: "https://maps.google.com/?q=Cairo+Takeaway+Newtown"
    },
    {
      name: "Bella Brutta",
      rating: "4.4",
      reviews: "620+",
      price: "中等",
      lat: -33.8988,
      lng: 151.1782,
      desc: "以拿坡里窯烤比薩聞名 Inner West，餅皮 Q 彈、配料極具創意。",
      childFriendly: "披薩絕對是親子最安全的用餐選項，有經典瑪格麗特與起司披薩可選。",
      mapsUrl: "https://maps.google.com/?q=Bella+Brutta+Newtown"
    },
    {
      name: "Pastizzi Cafe",
      rating: "4.5",
      reviews: "1,200+",
      price: "實惠",
      lat: -33.8959,
      lng: 151.1812,
      desc: "馬爾他傳統酥皮起司鹹點專賣店，口感香酥、價格親民，是 Newtown 傳奇老店。",
      childFriendly: "一口大小的手工酥皮餅（Pastizzi）奶香十足、酥脆可口，是完美的小點心。",
      mapsUrl: "https://maps.google.com/?q=Pastizzi+Cafe+Newtown"
    },
    {
      name: "Odd Culture Newtown",
      rating: "4.5",
      reviews: "520+",
      price: "中高",
      lat: -33.8964,
      lng: 151.1802,
      desc: "主打自然發酵食材與法式小酒館精緻歐陸料理，全天候營業，氣氛活潑。",
      childFriendly: "白天氣氛輕鬆溫馨，提供的招牌豬五花漢堡與自製發酵麵包味道絕佳。",
      mapsUrl: "https://maps.google.com/?q=Odd+Culture"
    }
  ],
  "Sydney CBD": [
    {
      name: "Chat Thai (Westfield Sydney)",
      rating: "4.2",
      reviews: "1,500+",
      price: "中等",
      lat: -33.8702,
      lng: 151.2085,
      desc: "雪梨最火紅的泰式料理 Westfield 分店，泰式炒河粉與雞肉沙嗲非常地道。",
      childFriendly: "炒河粉香甜不辣、沙嗲雞肉串甜香好入口，店內有充足嬰兒椅與兒童碗筷。",
      mapsUrl: "https://maps.google.com/?q=Chat+Thai+Westfield+Sydney"
    },
    {
      name: "New Shanghai (Westfield)",
      rating: "4.1",
      reviews: "1,250+",
      price: "中等",
      lat: -33.8704,
      lng: 151.2084,
      desc: "精緻江南中式點心店，以爆汁小籠包、生煎包與各式鍋貼聞名。",
      childFriendly: "湯汁飽滿的小籠包與生煎包是華人孩子的最愛，吃起來極具樂趣。",
      mapsUrl: "https://maps.google.com/?q=New+Shanghai+Westfield+Sydney"
    },
    {
      name: "Ippudo (一風堂 - Westfield)",
      rating: "4.2",
      reviews: "1,150+",
      price: "中等",
      lat: -33.8706,
      lng: 151.2086,
      desc: "來自日本博多的經典拉麵，湯頭濃郁、出餐極度迅速。",
      childFriendly: "拉麵不辣且湯頭醇厚，特別提供兒童專用拉麵碗筷，出餐快速省去小孩等待時間。",
      mapsUrl: "https://maps.google.com/?q=Ippudo+Westfield+Sydney"
    },
    {
      name: "Slim's Quality Burger",
      rating: "4.3",
      reviews: "350+",
      price: "實惠",
      lat: -33.8724,
      lng: 151.2078,
      desc: "復古美式漢堡店，主打現點現做牛肉漢堡、格子薯條與香濃巧克力奶昔。",
      childFriendly: "7歲男童漢堡天堂！復古裝潢配上手指薯條與甜甜奶昔，是最佳獎勵餐點。",
      mapsUrl: "https://maps.google.com/?q=Slim's+Quality+Burger+Sydney"
    },
    {
      name: "Fratelli Fresh (Westfield Sydney)",
      rating: "4.1",
      reviews: "2,100+",
      price: "中等",
      lat: -33.8703,
      lng: 151.2083,
      desc: "大型義式休閒餐飲，氣氛喧鬧活潑，特別針對親子家庭設計菜單。",
      childFriendly: "設有 Kid's Menu（經典義大利麵與個人比薩），週日有時還享有兒童用餐免費優惠。",
      mapsUrl: "https://maps.google.com/?q=Fratelli+Fresh+Westfield+Sydney"
    }
  ],
  "Blue Mountains": [
    {
      name: "Leura Garage",
      rating: "4.5",
      reviews: "1,300+",
      price: "中等",
      lat: -33.7095,
      lng: 150.3325,
      desc: "藍山獲獎名店，改建自舊汽車修理廠，保留輪胎、起重機等工業風裝潢。",
      childFriendly: "7歲男童超愛！可以在滿是機車零件與修理工具的車庫內大口吃松露野菇比薩與烤雞。",
      mapsUrl: "https://maps.google.com/?q=Leura+Garage+Leura"
    },
    {
      name: "The Bunker Leura",
      rating: "4.4",
      reviews: "1,150+",
      price: "中等",
      lat: -33.7112,
      lng: 150.3308,
      desc: "位於歷史悠久的莊園花園中，擁有大片綠意草坪，提供高品質早午餐與漢堡。",
      childFriendly: "擁有大片安全草地可以讓小孩奔跑放電，備有極佳的兒童漢堡與麵食選單。",
      mapsUrl: "https://maps.google.com/?q=The+Bunker+Leura"
    },
    {
      name: "Sanwiye Korean Cafe",
      rating: "4.8",
      reviews: "420+",
      price: "中等偏低",
      lat: -33.7126,
      lng: 150.3123,
      desc: "在卡通巴寒冷氣溫下，Google 評分高達 4.8 的奇蹟韓式家庭小餐館。",
      childFriendly: "香脆美味的韓式炸雞（可要求不辣的原味或甜醬），美味多汁，小孩吃得欲罷不能。",
      mapsUrl: "https://maps.google.com/?q=Sanwiye+Korean+Cafe+Katoomba"
    },
    {
      name: "Echoes Restaurant & Bar",
      rating: "4.4",
      reviews: "720+",
      price: "中高",
      lat: -33.7318,
      lng: 150.3115,
      desc: "緊鄰峭壁懸崖的景觀餐廳，全景玻璃窗可俯瞰三姊妹峰與 Jamison 峽谷大景。",
      childFriendly: "建議中午或下午茶時段去，天色明亮能看老鷹飛翔，氣氛較為放鬆。",
      mapsUrl: "https://maps.google.com/?q=Echoes+Restaurant+Katoomba"
    },
    {
      name: "The Wayzgoose Diner",
      rating: "4.3",
      reviews: "420+",
      price: "中等偏低",
      lat: -33.7086,
      lng: 150.3321,
      desc: "蘿拉小鎮上以傳統英式「花盆司康（Flowerpot Scone）」出名的高人氣美式復古餐館。",
      childFriendly: "懷舊的裝潢與超大草莓奶昔、薯條是絕配，花盆司康造型獨特有趣。",
      mapsUrl: "https://maps.google.com/?q=The+Wayzgoose+Diner+Leura"
    }
  ],
  "Darling Harbour": [
    {
      name: "Hurricane's Grill & Bar",
      rating: "4.3",
      reviews: "4,100+",
      price: "中等",
      lat: -33.8718,
      lng: 151.2008,
      desc: "雪梨最有名、最熱門的「碳烤豬排/牛排地標」，炭火香氣濃厚、份量大。",
      childFriendly: "氣氛喧鬧活潑，不用擔心小孩吵，招牌炭烤豬肋排甜鹹骨肉分離，小孩用手拿著吃非常開心。",
      mapsUrl: "https://maps.google.com/?q=Hurricane's+Grill+Darling+Harbour"
    },
    {
      name: "XOPP by Golden Century",
      rating: "4.3",
      reviews: "520+",
      price: "中高",
      lat: -33.8767,
      lng: 151.2023,
      desc: "傳奇粵菜金唐海鮮的精緻時尚分店，招牌「XO 醬蜆肉拌煎麵」是雪梨美食地標。",
      childFriendly: "經典廣式炒飯、清蒸魚片等，清淡美味，極適合家庭聚餐分享。",
      mapsUrl: "https://maps.google.com/?q=XOPP+Sydney"
    },
    {
      name: "Dopa Donburi & Milkbar",
      rating: "4.4",
      reviews: "510+",
      price: "中等偏低",
      lat: -33.8763,
      lng: 151.2028,
      desc: "網紅極力推崇的和牛丼飯與日式抹茶刨冰下午茶名店，食材新鮮美味。",
      childFriendly: "和牛燒肉蓋飯香甜軟嫩，焦糖布丁與草莓刨冰視覺與味覺都是小孩的最愛。",
      mapsUrl: "https://maps.google.com/?q=Dopa+Donburi+&amp;+Milkbar+Darling+Square"
    },
    {
      name: "Hello Auntie",
      rating: "4.2",
      reviews: "620+",
      price: "中等",
      lat: -33.8765,
      lng: 151.2025,
      desc: "創意精緻的現代越南料理，牛肉湯河粉湯頭以牛骨熬製多時，鮮甜無比。",
      childFriendly: "暖熱的牛肉湯河粉麵條滑溜，非常適合小朋友吸吮，雞肉春捲也很受歡迎。",
      mapsUrl: "https://maps.google.com/?q=Hello+Auntie+Darling+Square"
    },
    {
      name: "Pancakes On The Rocks (達令港分店)",
      rating: "4.1",
      reviews: "3,200+",
      price: "中等偏低",
      lat: -33.8724,
      lng: 151.1993,
      desc: "雪梨傳奇鬆餅老店，提供巨無霸美式甜鬆餅、烤肋排與披薩，極富歡樂色彩。",
      childFriendly: "家庭客比例高，香蕉巧克力鬆餅與烤豬肋排是經典的親子分享菜色。",
      mapsUrl: "https://maps.google.com/?q=Pancakes+On+The+Rocks+Darling+Harbour"
    }
  ],
  "Sydney Fish Market": [
    {
      name: "Vic's Meat Market",
      rating: "4.3",
      reviews: "520+",
      price: "中等",
      lat: -33.8727,
      lng: 151.1925,
      desc: "魚市場內最強德州 slow-smoked 慢燻烤肉店，慢火燻烤和牛胸肉軟嫩多汁。",
      childFriendly: "如果不吃生冷海鮮，這家的德州手撕豬肉堡與香脆薯條是 7 歲小朋友的最佳中餐。",
      mapsUrl: "https://maps.google.com/?q=Vic's+Meat+Market+Sydney"
    },
    {
      name: "Blackwattle Deli",
      rating: "4.4",
      reviews: "210+",
      price: "中等",
      lat: -33.8729,
      lng: 151.1928,
      desc: "魚市場二樓的隱藏版精緻起司熟食店，露台吧台區享有絕佳避開人群的無敵海景。",
      childFriendly: "氣氛相對安靜，現烤的魯本起司三明治料多實在，可帶小孩安靜看海景與漁船。",
      mapsUrl: "https://maps.google.com/?q=Blackwattle+Deli+Sydney"
    },
    {
      name: "Sokyo (Pyrmont)",
      rating: "4.5",
      reviews: "1,850+",
      price: "高檔",
      lat: -33.8682,
      lng: 151.1945,
      desc: "魚市場旁 The Star 酒店內的高檔創意日料天花板，多次榮獲雪梨餐飲大獎認證。",
      childFriendly: "中午時段氣氛較為休閒，精緻日式 Bento 盒包含炸天婦羅與兒童喜愛的壽司細卷。",
      mapsUrl: "https://maps.google.com/?q=Sokyo+Pyrmont"
    },
    {
      name: "Peter's Sydney Fish Market",
      rating: "4.0",
      reviews: "2,100+",
      price: "中等",
      lat: -33.8725,
      lng: 151.1922,
      desc: "魚市場最核心的海鮮選購與現場烹飪加工大排檔，海鮮現撈現煮極為新鮮。",
      childFriendly: "有大量的黃金炸海鮮拼盤、芝士焗扇貝熟食，符合小孩喜好。",
      mapsUrl: "https://maps.google.com/?q=Peter's+Fish+Market"
    },
    {
      name: "Biaggio Cafe (Pyrmont)",
      rating: "4.3",
      reviews: "410+",
      price: "中等偏低",
      lat: -33.8719,
      lng: 151.1932,
      desc: "魚市場外步行 3 分鐘，安靜舒適的義大利咖啡餐館，提供經典手工披薩與麵食。",
      childFriendly: "避開魚市場內喧囂擁擠，舒適坐下享用番茄肉醬麵（Bolognese）與兒童比薩，極其省力。",
      mapsUrl: "https://maps.google.com/?q=Biaggio+Cafe+Pyrmont"
    }
  ]
};


