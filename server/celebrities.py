"""
Celebrity Voice Database for Indian Cinema Stars
Contains comprehensive information about celebrities across different film industries
"""

CELEBRITIES_DATABASE = {
    "bollywood": [
        {
            "id": "amitabh_bachchan",
            "name": "Amitabh Bachchan",
            "image": "https://images.indianexpress.com/2024/10/Happy-birthday-Mr-Amitabh-Bachchan.jpg",
            "bio": "Legendary Bollywood actor known as the 'Shahenshah' of Indian cinema. With a career spanning over five decades, he's known for his deep, authoritative voice and iconic dialogue delivery.",
            "voice_sample": "/samples/amitabh_bachchan_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 98,
            "debut_year": 1969,
            "notable_films": ["Sholay", "Deewaar", "Zanjeer", "Don", "Piku"],
            "voice_characteristics": ["deep", "authoritative", "baritone", "commanding"],
            "category": "bollywood"
        },
        {
            "id": "shah_rukh_khan",
            "name": "Shah Rukh Khan",
            "image": "https://filmfare.wwmindia.com/content/2018/feb/shah-rukh-khan_filmfare_bollywoodtadkamasala_blogspot_com__3_1518023440.jpg",
            "bio": "The 'King of Bollywood' known for his romantic roles and charismatic screen presence. His voice is smooth, expressive, and instantly recognizable across the globe.",
            "voice_sample": "/samples/shah_rukh_khan_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 97,
            "debut_year": 1992,
            "notable_films": ["Dilwale Dulhania Le Jayenge", "My Name is Khan", "Chennai Express", "Raees"],
            "voice_characteristics": ["romantic", "charismatic", "smooth", "expressive"],
            "category": "bollywood"
        },
        {
            "id": "aamir_khan",
            "name": "Aamir Khan",
            "image": "https://i2.cinestaan.com/image-bank/1500-1500/126001-127000/126991.jpg",
            "bio": "Known as 'Mr. Perfectionist', Aamir Khan is renowned for his versatile acting and distinctive voice that adapts to various characters with remarkable precision.",
            "voice_sample": "/samples/aamir_khan_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 95,
            "debut_year": 1988,
            "notable_films": ["Lagaan", "3 Idiots", "Dangal", "Taare Zameen Par"],
            "voice_characteristics": ["versatile", "precise", "emotional", "adaptable"],
            "category": "bollywood"
        },
        {
            "id": "salman_khan",
            "name": "Salman Khan",
            "image": "https://i2.cinestaan.com/image-bank/1500-1500/124001-125000/124850.jpg",
            "bio": "The 'Bhai' of Bollywood, known for his energetic performances and distinctive voice that resonates with millions of fans across the country.",
            "voice_sample": "/samples/salman_khan_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 96,
            "debut_year": 1988,
            "notable_films": ["Hum Aapke Hain Koun", "Bajrangi Bhaijaan", "Sultan", "Tiger Zinda Hai"],
            "voice_characteristics": ["energetic", "bold", "confident", "powerful"],
            "category": "bollywood"
        },
        {
            "id": "deepika_padukone",
            "name": "Deepika Padukone",
            "image": "/images/celebrities/deepika_padukone.jpg",
            "bio": "One of India's highest-paid actresses, known for her elegant voice and powerful performances in both commercial and critically acclaimed films.",
            "voice_sample": "/samples/deepika_padukone_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 94,
            "debut_year": 2007,
            "notable_films": ["Padmaavat", "Chennai Express", "Piku", "Chhapaak"],
            "voice_characteristics": ["elegant", "clear", "sophisticated", "melodious"],
            "category": "bollywood"
        },
        {
            "id": "priyanka_chopra",
            "name": "Priyanka Chopra",
            "image": "/images/celebrities/priyanka_chopra.jpg",
            "bio": "Global icon and former Miss World, known for her confident voice and international appeal. Her voice carries both Indian warmth and global sophistication.",
            "voice_sample": "/samples/priyanka_chopra_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 93,
            "debut_year": 2003,
            "notable_films": ["Fashion", "Mary Kom", "The Sky Is Pink", "Quantico"],
            "voice_characteristics": ["confident", "international", "versatile", "strong"],
            "category": "bollywood"
        },
        {
            "id": "hrithik_roshan",
            "name": "Hrithik Roshan",
            "image": "/images/celebrities/hrithik_roshan.jpg",
            "bio": "Known as the 'Greek God' of Bollywood, Hrithik's voice is as smooth and sophisticated as his dance moves, perfect for romantic and action roles.",
            "voice_sample": "/samples/hrithik_roshan_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 92,
            "debut_year": 2000,
            "notable_films": ["Kaho Naa... Pyaar Hai", "Zindagi Na Milegi Dobara", "War", "Super 30"],
            "voice_characteristics": ["smooth", "sophisticated", "romantic", "clear"],
            "category": "bollywood"
        },
        {
            "id": "akshay_kumar",
            "name": "Akshay Kumar",
            "image": "/images/celebrities/akshay_kumar.jpg",
            "bio": "The 'Khiladi' of Bollywood, known for his energetic voice and ability to excel in action, comedy, and social drama films.",
            "voice_sample": "/samples/akshay_kumar_sample.mp3",
            "languages": ["hindi", "english"],
            "popularity": 91,
            "debut_year": 1991,
            "notable_films": ["Hera Pheri", "Toilet: Ek Prem Katha", "Pad Man", "Mission Mangal"],
            "voice_characteristics": ["energetic", "clear", "versatile", "commanding"],
            "category": "bollywood"
        }
    ],
    "tollywood": [
        {
            "id": "prabhas",
            "name": "Prabhas",
            "image": "/images/celebrities/prabhas.jpg",
            "bio": "The 'Darling' of Tollywood who gained international fame with Baahubali series. His voice carries the power and heroism that made him a pan-Indian star.",
            "voice_sample": "/samples/prabhas_sample.mp3",
            "languages": ["telugu", "hindi", "english"],
            "popularity": 96,
            "debut_year": 2002,
            "notable_films": ["Baahubali", "Saaho", "Radhe Shyam", "Adipurush"],
            "voice_characteristics": ["powerful", "heroic", "deep", "commanding"],
            "category": "tollywood"
        },
        {
            "id": "mahesh_babu",
            "name": "Mahesh Babu",
            "image": "/images/celebrities/mahesh_babu.jpg",
            "bio": "The 'Prince' of Tollywood, known for his sophisticated voice and stylish screen presence. His voice perfectly complements his suave personality.",
            "voice_sample": "/samples/mahesh_babu_sample.mp3",
            "languages": ["telugu", "hindi", "english"],
            "popularity": 95,
            "debut_year": 1999,
            "notable_films": ["Pokiri", "Dookudu", "Srimanthudu", "Sarileru Neekevvaru"],
            "voice_characteristics": ["sophisticated", "smooth", "stylish", "clear"],
            "category": "tollywood"
        },
        {
            "id": "jr_ntr",
            "name": "Jr. NTR",
            "image": "/images/celebrities/jr_ntr.jpg",
            "bio": "Known for his dynamic performances and emotional range, Jr. NTR's voice is as versatile as his acting, capable of both intense drama and light comedy.",
            "voice_sample": "/samples/jr_ntr_sample.mp3",
            "languages": ["telugu", "hindi", "english"],
            "popularity": 94,
            "debut_year": 2001,
            "notable_films": ["RRR", "Janatha Garage", "Aravinda Sametha", "Jai Lava Kusa"],
            "voice_characteristics": ["dynamic", "emotional", "versatile", "intense"],
            "category": "tollywood"
        },
        {
            "id": "ram_charan",
            "name": "Ram Charan",
            "image": "/images/celebrities/ram_charan.jpg",
            "bio": "The 'Mega Power Star' who gained global recognition with RRR. His voice carries the legacy of his father Chiranjeevi with a modern touch.",
            "voice_sample": "/samples/ram_charan_sample.mp3",
            "languages": ["telugu", "hindi", "english"],
            "popularity": 93,
            "debut_year": 2007,
            "notable_films": ["RRR", "Rangasthalam", "Magadheera", "Dhruva"],
            "voice_characteristics": ["charismatic", "strong", "modern", "powerful"],
            "category": "tollywood"
        },
        {
            "id": "samantha",
            "name": "Samantha Ruth Prabhu",
            "image": "/images/celebrities/samantha.jpg",
            "bio": "One of the most popular actresses in South Indian cinema, known for her sweet yet strong voice that perfectly captures both vulnerability and strength.",
            "voice_sample": "/samples/samantha_sample.mp3",
            "languages": ["telugu", "tamil", "hindi", "english"],
            "popularity": 92,
            "debut_year": 2010,
            "notable_films": ["Eega", "Theri", "Rangasthalam", "The Family Man 2"],
            "voice_characteristics": ["sweet", "versatile", "strong", "melodious"],
            "category": "tollywood"
        },
        {
            "id": "rashmika_mandanna",
            "name": "Rashmika Mandanna",
            "image": "/images/celebrities/rashmika_mandanna.jpg",
            "bio": "The 'National Crush' known for her youthful energy and expressive voice that resonates with the younger generation across India.",
            "voice_sample": "/samples/rashmika_mandanna_sample.mp3",
            "languages": ["telugu", "kannada", "hindi", "english"],
            "popularity": 90,
            "debut_year": 2016,
            "notable_films": ["Pushpa", "Dear Comrade", "Geetha Govindam", "Mission Majnu"],
            "voice_characteristics": ["youthful", "energetic", "expressive", "bubbly"],
            "category": "tollywood"
        }
    ],
    "kollywood": [
        {
            "id": "rajinikanth",
            "name": "Rajinikanth",
            "image": "/images/celebrities/rajinikanth.jpg",
            "bio": "The 'Superstar' of Indian cinema, known for his iconic style and distinctive voice that has entertained audiences for over four decades.",
            "voice_sample": "/samples/rajinikanth_sample.mp3",
            "languages": ["tamil", "hindi", "english"],
            "popularity": 99,
            "debut_year": 1975,
            "notable_films": ["Baasha", "Sivaji", "Enthiran", "Kabali"],
            "voice_characteristics": ["iconic", "stylish", "powerful", "distinctive"],
            "category": "kollywood"
        },
        {
            "id": "vijay",
            "name": "Vijay",
            "image": "/images/celebrities/vijay1.jpg",
            "bio": "The 'Thalapathy' of Tamil cinema, known for his energetic performances and youthful voice that appeals to fans across all age groups.",
            "voice_sample": "/samples/vijay_sample.mp3",
            "languages": ["tamil", "hindi", "english"],
            "popularity": 97,
            "debut_year": 1992,
            "notable_films": ["Ghilli", "Thuppakki", "Mersal", "Master"],
            "voice_characteristics": ["energetic", "youthful", "dynamic", "appealing"],
            "category": "kollywood"
        },
        {
            "id": "kamal_haasan",
            "name": "Kamal Haasan",
            "image": "/images/celebrities/kamal_haasan.jpg",
            "bio": "The 'Ulaganayagan' (Universal Hero), known for his intellectual approach to cinema and versatile voice that adapts to any character or genre.",
            "voice_sample": "/samples/kamal_haasan_sample.mp3",
            "languages": ["tamil", "hindi", "english", "telugu"],
            "popularity": 96,
            "debut_year": 1960,
            "notable_films": ["Nayakan", "Indian", "Vishwaroopam", "Vikram"],
            "voice_characteristics": ["intellectual", "versatile", "sophisticated", "varied"],
            "category": "kollywood"
        },
        {
            "id": "suriya",
            "name": "Suriya",
            "image": "/images/celebrities/suriya.jpg",
            "bio": "Known for his intense performances and passionate voice, Suriya has established himself as one of the finest actors in Tamil cinema.",
            "voice_sample": "/samples/suriya_sample.mp3",
            "languages": ["tamil", "hindi", "english"],
            "popularity": 94,
            "debut_year": 1997,
            "notable_films": ["Ghajini", "Singam", "Soorarai Pottru", "Jai Bhim"],
            "voice_characteristics": ["intense", "passionate", "emotional", "strong"],
            "category": "kollywood"
        },
        {
            "id": "dhanush",
            "name": "Dhanush",
            "image": "/images/celebrities/dhanush.jpg",
            "bio": "The versatile actor known for his unique voice and ability to portray diverse characters. His voice has a distinctive quality that's both rustic and refined.",
            "voice_sample": "/samples/dhanush_sample.mp3",
            "languages": ["tamil", "hindi", "english"],
            "popularity": 93,
            "debut_year": 2002,
            "notable_films": ["Asuran", "Karnan", "Raanjhanaa", "Atrangi Re"],
            "voice_characteristics": ["unique", "expressive", "versatile", "distinctive"],
            "category": "kollywood"
        },
        {
            "id": "nayanthara",
            "name": "Nayanthara",
            "image": "/images/celebrities/nayanthara.jpg",
            "bio": "The 'Lady Superstar' of South Indian cinema, known for her confident voice and strong screen presence that commands respect and admiration.",
            "voice_sample": "/samples/nayanthara_sample.mp3",
            "languages": ["tamil", "telugu", "malayalam", "hindi"],
            "popularity": 92,
            "debut_year": 2003,
            "notable_films": ["Aramm", "Kolamavu Kokila", "Netrikann", "Connect"],
            "voice_characteristics": ["confident", "strong", "clear", "commanding"],
            "category": "kollywood"
        }
    ],
    "regional": [
        {
            "id": "yash",
            "name": "Yash",
            "image": "/images/celebrities/yash.jpg",
            "bio": "The 'Rocking Star' of Kannada cinema who gained pan-Indian fame with the KGF series. His voice carries the ruggedness and intensity of his characters.",
            "voice_sample": "/samples/yash_sample.mp3",
            "languages": ["kannada", "hindi", "english"],
            "popularity": 95,
            "debut_year": 2007,
            "notable_films": ["KGF Chapter 1", "KGF Chapter 2", "Masterpiece", "Googly"],
            "voice_characteristics": ["rugged", "intense", "powerful", "distinctive"],
            "category": "regional"
        },
        {
            "id": "dulquer_salmaan",
            "name": "Dulquer Salmaan",
            "image": "/images/celebrities/dulquer_salmaan.jpg",
            "bio": "The versatile Malayalam actor known for his charming voice and pan-Indian appeal. His voice perfectly complements his boy-next-door image.",
            "voice_sample": "/samples/dulquer_salmaan_sample.mp3",
            "languages": ["malayalam", "tamil", "hindi", "english"],
            "popularity": 91,
            "debut_year": 2012,
            "notable_films": ["Charlie", "Bangalore Days", "Karwaan", "The Zoya Factor"],
            "voice_characteristics": ["charming", "versatile", "smooth", "appealing"],
            "category": "regional"
        },
        {
            "id": "allu_arjun",
            "name": "Allu Arjun",
            "image": "/images/celebrities/allu_arjun.jpg",
            "bio": "The 'Stylish Star' known for his unique dialogue delivery and stylish screen presence. His voice became nationally famous with Pushpa.",
            "voice_sample": "/samples/allu_arjun_sample.mp3",
            "languages": ["telugu", "hindi", "english"],
            "popularity": 94,
            "debut_year": 2003,
            "notable_films": ["Pushpa", "Ala Vaikunthapurramuloo", "Sarrainodu", "DJ"],
            "voice_characteristics": ["stylish", "unique", "trendy", "distinctive"],
            "category": "regional"
        },
        {
            "id": "fahadh_faasil",
            "name": "Fahadh Faasil",
            "image": "/images/celebrities/fahadh_faasil.jpg",
            "bio": "The critically acclaimed Malayalam actor known for his intense and nuanced voice that brings depth to every character he portrays.",
            "voice_sample": "/samples/fahadh_faasil_sample.mp3",
            "languages": ["malayalam", "tamil", "hindi", "english"],
            "popularity": 89,
            "debut_year": 2002,
            "notable_films": ["Kumbakonam Gopals", "Thondimuthalum Driksakshiyum", "Super Deluxe", "Pushpa"],
            "voice_characteristics": ["intense", "nuanced", "sophisticated", "deep"],
            "category": "regional"
        }
    ]
}

def get_all_celebrities():
    """Get all celebrities from all categories"""
    all_celebrities = []
    for category, celebrities in CELEBRITIES_DATABASE.items():
        all_celebrities.extend(celebrities)
    return all_celebrities

def get_celebrities_by_category(category):
    """Get celebrities by specific category"""
    return CELEBRITIES_DATABASE.get(category, [])

def get_celebrity_by_id(celebrity_id):
    """Get specific celebrity by ID"""
    for category, celebrities in CELEBRITIES_DATABASE.items():
        for celebrity in celebrities:
            if celebrity["id"] == celebrity_id:
                return celebrity
    return None

def get_categories():
    """Get all available categories"""
    return list(CELEBRITIES_DATABASE.keys())

def search_celebrities(query):
    """Search celebrities by name or characteristics"""
    query = query.lower()
    results = []
    
    for category, celebrities in CELEBRITIES_DATABASE.items():
        for celebrity in celebrities:
            if (query in celebrity["name"].lower() or 
                query in celebrity["bio"].lower() or
                any(query in char.lower() for char in celebrity["voice_characteristics"])):
                results.append(celebrity)
    
    return results