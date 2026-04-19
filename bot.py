# -*- coding: utf-8 -*-
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@techmind_uz_main"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_lang = {}

# ====== TEXT BUTTONS ======
DATA = {
    "uz": {
        "lang": "Tilni tanlang 🌐",
        "main": "Kerakli bo‘limni tanlang 👇",
        "strategy": "📊 Aniq strategiya",
        "uni": "🎓 Universitetlar",
        "net": "🌐 Bizning tarmoqlar",
        "contact": "📩 Bog'lanish",
        "settings": "⚙️ Sozlamalar",
        "back": "🔙 Orqaga",
        "directions": "📚 Yo'nalishlar",
        "ai": "🤖 AI",
        "cyber": "🛡️ Kiberxavfsizlik",
        "robot": "🤖 Robototexnika",
        "subscribe": "❗ Kanalga obuna bo‘ling",
        "check": "✅ Tekshirish",
        "change_lang": "🌐 Tilni o‘zgartirish"
    },
    "ru": {
        "lang": "Выберите язык 🌐",
        "main": "Выберите раздел 👇",
        "strategy": "📊 Стратегия",
        "uni": "🎓 Университеты",
        "net": "🌐 Наши сети",
        "contact": "📩 Связь",
        "settings": "⚙️ Настройки",
        "back": "🔙 Назад",
        "directions": "📚 Направления",
        "ai": "🤖 AI",
        "cyber": "🛡️ Кибербезопасность",
        "robot": "🤖 Робототехника",
        "subscribe": "❗ Подпишитесь на канал",
        "check": "✅ Проверить",
        "change_lang": "🌐 Сменить язык"
    },
    "en": {
        "lang": "Choose language 🌐",
        "main": "Choose section 👇",
        "strategy": "📊 Strategy",
        "uni": "🎓 Universities",
        "net": "🌐 Our networks",
        "contact": "📩 Contact",
        "settings": "⚙️ Settings",
        "back": "🔙 Back",
        "directions": "📚 Directions",
        "ai": "🤖 AI",
        "cyber": "🛡️ Cybersecurity",
        "robot": "🤖 Robotics",
        "subscribe": "❗ Subscribe to channel",
        "check": "✅ Check",
        "change_lang": "🌐 Change language"
    }
}

# ====== CONTENT (SEN TO'LDIRASAN) ======
CONTENT = {
    "strategy": {
        "uz":"""Universitetlarga 100% Grant Asosida Kirish Strategiyasi
​Tabriklaymiz! Siz kelajakning eng nufuzli sohalaridan birini tanladingiz. AI (Sun'iy intellekt), Kiberxavfsizlik va Robototexnika yo‘nalishlari bo‘yicha dunyoning top universitetlarida bepul o‘qish uchun quyidagi 5 bosqichli strategiyani amalga oshirishingiz lozim:

​1️⃣ Akademik Tayyorgarlik va Poydevor
​Ushbu sohalar muhandislik va yuqori mantiqiy fikrlashni talab qiladi.

​Matematika va Fizika: Calculus, ehtimollar nazariyasi va chiziqli algebra fanlarini mukammal o‘zlashtiring.

​GPA (O‘rtacha baho): Maktab yoki kollej shahodatnomangizdagi ko‘rsatkichlar kamida 4.5 (yoki 90%) bo‘lishi tavsiya etiladi.

​SAT/ACT: Xalqaro darajadagi grantlar uchun SAT imtihonidan 1450+ ball olish imkoniyatlaringizni keskin oshiradi.

​2️⃣ Til Bilish Sertifikatlari
​Bepul ta’lim va xalqaro grantlar uchun til — asosiy kalit hisoblanadi.
​Ingliz tili: Kamida IELTS 7.0 yoki TOEFL 95+ ball.

​Yevropa imkoniyatlari: Agar nemis (C1) yoki italyan tilini o‘rgansangiz, Germaniya va Italiya davlat universitetlarida mutlaqo bepul ta’lim olishingiz mumkin.

​3️⃣ Amaliy Portfolio (Extra-curricular)
​Top universitetlar faqat baholarga emas, balki sizning amaliy qobiliyatingizga ham e’tibor qaratadi:

​AI yo‘nalishi uchun: Python tilini o‘rganing va Kaggle platformasidagi loyihalarda ishtirok eting.

​Kiberxavfsizlik uchun: CTF (Capture The Flag) musobaqalarida qatnashing va platformalardan (TryHackMe, HackTheBox) sertifikatlar to‘plang.

​Robototexnika uchun: Arduino yoki Raspberry Pi bazasida mustaqil loyihalar yarating va ularning ishlash jarayonini videoga muhrlang.

​4️⃣ To‘g‘ri Universitet va Grant Dasturini Tanlash
​Har bir yo‘nalish bo‘yicha eng samarali bepul dasturlar:

​Germaniya (DAAD): Ta’lim bepul, ko‘plab ingliz tilidagi dasturlar mavjud.

​Vengriya (Stipendium Hungaricum): O‘qish, turar joy va oylik stipendiya 100% qoplanadi.

​Janubiy Koreya (GKS): IT va texnologiya yo‘nalishida dunyodagi eng nufuzli to‘liq grantlardan biri.

​AQSH (Need-blind Grantlar): MIT, Stanford va Harvard kabi universitetlar iqtidorli talabalarning barcha xarajatlarini qoplab berishi mumkin.

​5️⃣ Shaxsiy Bayonnomo (Motivation Letter)
​Bu sizning arizangizning eng muhim qismidir. Unda quyidagi savollarga aniq javob bering:
​"Nega aynan ushbu sohani tanladingiz? Kelajakda qaysi global muammoni hal qilmoqchisiz? Sizning intilishlaringiz jamiyat rivojiga qanday hissa qo‘shadi?"

​💡 Muhim Maslahat:
​Hujjat topshirish jarayonini kamida 1 yil oldin rejalashtiring. Aksariyat xalqaro grantlar uchun qabul jarayoni sentyabr va yanvar oylari oralig‘ida bo‘lib o‘tadi.
​Eslatma: Texnologiyalar dunyosida eng katta investitsiya — bu sizning bilimingizdir. Bugundan harakatni boshlang!""",

        "ru": """Стратегия поступления в университеты на 100% грант

🚀 Поздравляем! Вы выбрали одну из самых перспективных сфер будущего. Чтобы бесплатно учиться в топовых университетах мира по направлениям AI (искусственный интеллект), кибербезопасность и робототехника, вам необходимо реализовать следующую стратегию из 5 шагов:

1️⃣ Академическая подготовка и фундамент

Эти направления требуют инженерного мышления и высокой логики.

Математика и физика: Освойте Calculus, теорию вероятностей и линейную алгебру на высоком уровне.

GPA (средний балл): Желательно не ниже 4.5 (или 90%).

SAT/ACT: Балл 1450+ значительно увеличит ваши шансы на получение гранта.

2️⃣ Сертификаты по языкам

Язык — ключ к международным грантам.

Английский язык: Минимум IELTS 7.0 или TOEFL 95+

Европейские возможности: Знание немецкого (C1) или итальянского открывает доступ к бесплатному обучению в Германии и Италии

3️⃣ Практическое портфолио (Extra-curricular)

Топовые университеты оценивают не только оценки, но и навыки:

Для AI: Изучите Python и участвуйте в проектах на Kaggle

Для кибербезопасности: Участвуйте в CTF-соревнованиях и получайте сертификаты (TryHackMe, HackTheBox)

Для робототехники: Создавайте проекты на Arduino или Raspberry Pi и записывайте процесс

4️⃣ Выбор университета и гранта

Германия (DAAD): Бесплатное обучение, множество программ на английском

Венгрия (Stipendium Hungaricum): Полное покрытие обучения, жилья и стипендия

Южная Корея (GKS): Один из лучших IT-грантов в мире

США (Need-blind): MIT, Stanford, Harvard могут полностью покрыть расходы

5️⃣ Мотивационное письмо

Самая важная часть заявки:

Почему вы выбрали эту сферу?
Какую глобальную проблему хотите решить?
Как вы повлияете на общество?

💡 Важно:
Начинайте подготовку минимум за 1 год. Большинство заявок подаются с сентября по январь.

📌 Технологии — это инвестиция в ваше будущее. Начните сегодня!""",

        "en": """Strategy to Enter Universities with a 100% Scholarship
🚀 Congratulations! You have chosen one of the most prestigious fields of the future. To study for free at top universities worldwide in AI (Artificial Intelligence), Cybersecurity, and Robotics, you should follow this 5-step strategy:
1️⃣ Academic Preparation and Foundation
These fields require engineering skills and strong logical thinking.
Mathematics & Physics: Master Calculus, Probability Theory, and Linear Algebra
GPA: Aim for at least 4.5 (or 90%)
SAT/ACT: A score of 1450+ significantly boosts your chances

2️⃣ Language Certificates
Language is the key to international scholarships.
English: Minimum IELTS 7.0 or TOEFL 95+
European Opportunities: German (C1) or Italian can allow free education in Germany and Italy

3️⃣ Practical Portfolio (Extra-curricular)
Top universities value skills beyond grades:
For AI: Learn Python and participate in Kaggle projects
For Cybersecurity: Join CTF competitions and earn certificates (TryHackMe, HackTheBox)
For Robotics: Build projects using Arduino or Raspberry Pi and document them

4️⃣ Choosing the Right University & Scholarship
Germany (DAAD): Free education with many English programs
Hungary (Stipendium Hungaricum): Covers tuition, accommodation, and stipend
South Korea (GKS): One of the top fully funded IT scholarships
USA (Need-blind): MIT, Stanford, Harvard may cover all expenses

5️⃣ Motivation Letter
The most important part of your application:
Why did you choose this field?
What global problem do you want to solve?
How will you contribute to society?

💡 Important Tip:
Start preparing at least 1 year in advance. Most deadlines are between September and January.
📌 The biggest investment in technology is your knowledge. Start today!"""

    },
    "ai": {
        "uz": """​🏆 Dunyoning Eng Kuchli AI Grantlari (Top Tier)

​Ushbu universitetlarda o‘qish — bu kelajakdagi 100% muvaffaqiyat kafolatidir. Lekin raqobat juda kuchli.

​1. Massachusetts Institute of Technology (MIT) — AQSH

​Grant turi: Need-Blind Financial Aid. Agar siz o‘qishga qabul qilinsangiz, universitet oilaviy daromadingizga qarab barcha xarajatlarni (o'qish, yashash, ovqatlanish) o‘z zimmasiga oladi.

​Xususiyati: Dunyodagi AI bo‘yicha #1 universitet.

​Talablar: Mukammal matematika (SAT 1550+), kuchli shaxsiy loyihalar va xalqaro olimpiadalar.

​2. KAIST (Korea Advanced Institute of Science and Technology) — Janubiy Koreya

​Grant turi: KAIST International Student Scholarship. O‘qish bepul, oylik stipendiya (taxminan 300$) va tibbiy sug‘urta.

​Xususiyati: Osiyodagi eng kuchli texnologik OTM. Robototexnika va AI sohasida dunyo yetakchisi.

​Talablar: IELTS 6.5+, yuqori GPA va kuchli motivatsiya xati.

​✅ Qabul Qilinishi Oson va 100% Grant Beruvchi OTMlar
​Bu universitetlarda grant yutish ehtimoli yuqori, chunki ular hukumat dasturlari orqali ko‘p sonli talabalarni qabul qiladi.

​1. Eötvös Loránd University (ELTE) — Vengriya

​Grant turi: Stipendium Hungaricum. 100% bepul o‘qish, yotoqxona, tibbiy sug‘urta va oylik stipendiya.

​Xususiyati: Computer Science va AI yo‘nalishi bo‘yicha Markaziy Yevropadagi eng nufuzli universitet.

​Imkoniyat: Har yili O'zbekiston uchun yuzlab o‘rinlar ajratiladi. Qabul jarayoni shaffof va oson.

​2. Pisa Universiteti (University of Pisa) — Italiya

​Grant turi: DSU Scholarship. Oilaviy daromadingiz past bo‘lsa, o‘qish bepul bo‘ladi + yiliga taxminan 6,000–7,000 evro stipendiya beriladi.

​Xususiyati: Italiyadagi eng qadimgi va AI bo‘yicha eng kuchli maktablardan biri. "Artificial Intelligence and Data Science" dasturi juda mashhur.

​Imkoniyat: Italiyada grant yutish uchun faqat o‘qishga kirish va oilaviy daromad hujjatlarini to‘g‘ri topshirish kifoya (ko'pincha qo'shimcha imtihonsiz).

​"Agar sizga bilim va nom kerak bo‘lsa — MIT yoki KAISTni, agar 100% kafolatlangan moliyaviy yordam va Yevropa diplomi kerak bo‘lsa — ELTE yoki Italiya universitetlarini tanlang!""",

        "ru": """Самые сильные AI-гранты (Top Tier)

Обучение в этих университетах — почти 100% гарантия успешного будущего. Но конкуренция очень высокая.

Massachusetts Institute of Technology (MIT) — США

Тип гранта: Need-Blind Financial Aid. Если вы поступаете, университет покрывает все расходы (обучение, проживание, питание) в зависимости от дохода семьи.

Особенность: №1 в мире по AI.

Требования: SAT 1550+, сильные проекты и олимпиады.

KAIST (Korea Advanced Institute of Science and Technology) — Южная Корея

Тип гранта: Полностью бесплатное обучение, стипендия (~300$) и страховка.

Особенность: Один из лучших технологических вузов Азии.

Требования: IELTS 6.5+, высокий GPA и мотивационное письмо.

Университеты с более высоким шансом поступления и 100% грантом:

Eötvös Loránd University (ELTE) — Венгрия

Тип гранта: Stipendium Hungaricum (полное покрытие: учеба, жилье, стипендия).

Особенность: Сильный вуз по Computer Science и AI.

University of Pisa — Италия

Тип гранта: DSU Scholarship (бесплатное обучение + 6000–7000 евро в год).

Особенность: Один из старейших университетов с сильным AI направлением.

Итог:
Если нужен топ-уровень — MIT или KAIST.
Если важен гарантированный грант — ELTE или университеты Италии.""",

        "en": """Top AI Scholarships (Copy-Friendly Version)

Studying at these universities is almost a 100% guarantee of success, but competition is very high.

Massachusetts Institute of Technology (MIT) — USA

Scholarship: Need-Blind Financial Aid (covers all expenses).

Highlight: #1 in AI worldwide.

Requirements: SAT 1550+, strong projects and олимпиads.

KAIST (Korea Advanced Institute of Science and Technology) — South Korea

Scholarship: Free tuition + ~$300 stipend + insurance.

Highlight: Top tech university in Asia.

Requirements: IELTS 6.5+, high GPA, strong motivation letter.

Easier universities with full scholarships:

Eötvös Loránd University (ELTE) — Hungary

Scholarship: Stipendium Hungaricum (full coverage).

Highlight: Strong in Computer Science and AI.

University of Pisa — Italy

Scholarship: DSU (free tuition + €6000–7000/year).

Highlight: Historic university with strong AI programs.

Conclusion:
Top prestige → MIT or KAIST
Guaranteed funding → ELTE or Italian universities"""
    },
    "cyber": {
        "uz": """​🛡️ Kiberxavfsizlik Bo‘yicha Eng Kuchli Grantlar (Elite)

​Bu universitetlar kiberxavfsizlik dunyosining "markazi" hisoblanadi. Grant yutish qiyin, lekin diplomi butun dunyoda eshiklarni ochadi.

​1. Carnegie Mellon University (CMU) — AQSH

​Grant turi: CyberCorps: Scholarship for Service (SFS) va ichki moliyaviy yordamlar.

​Xususiyati: Kiberxavfsizlik bo‘yicha dunyo reytingida doimiy 1-o‘rinda turadi. Mashhur "CyLab" tadqiqot markaziga ega.

​Talablar: Juda yuqori akademik ko'rsatkichlar, mantiqiy testlar va dasturlash bo'yicha kuchli bilim.

​2. Tallinn University of Technology (TalTech) — Estoniya

​Grant turi: Estonian Government Scholarship. Estoniya kiberxavfsizlik bo‘yicha dunyo yetakchilaridan biri (NATO kiber-markazi shu yerda joylashgan).

​Xususiyati: "Cybersecurity" magistrlik dasturi butunlay ingliz tilida va grant asosida o‘qish imkoniyati yuqori.

​Talablar: IT bo‘yicha bakalavr diplomi, IELTS 6.0+ va kiber-musobaqalardagi (CTF) ishtirok.

​✅ Grant Yutish Oson va 100% Imkoniyat Beruvchi OTMlar
​Ushbu yo‘nalishlarda raqobat nisbatan kamroq yoki grant kvotalari ko'proq.

​1. University of Tartu — Estoniya

​Grant turi: Tuition-Waiver Scholarship. O‘qish pulini 100% qoplab beruvchi grantlar juda ko‘p ajratiladi.

​Xususiyati: Kriptografiya va elektron hukumat xavfsizligi bo‘yicha dunyodagi eng kuchli dasturlardan biriga ega.

​Imkoniyat: O‘zbekistonlik talabalar uchun Estoniya universitetlariga kirish va viza olish jarayoni boshqa Yevropa davlatlariga qaraganda ancha oson.

​2. TU Darmstadt — Germaniya
​Grant turi: DAAD yoki Deutschlandstipendium.

 Germaniyada davlat universitetlarida o‘qish deyarli bepul (semestr uchun kichik to'lov bor).

​Xususiyati: Germaniyaning kiberxavfsizlik bo‘yicha "poytaxti" hisoblanadi. "ATHENE" — Yevropadagi eng yirik kiberxavfsizlik tadqiqot markazi shu yerda joylashgan.

​Imkoniyat: Nemis tilini C1 darajada bilsangiz, qabul qilinish ehtimoli deyarli 100%. Ingliz tilidagi dasturlarga esa IELTS 6.5+ bilan kirish mumkin.
​
​"Kiberxavfsizlik sohasida faqat nazariya bilan grant yutib bo‘lmaydi. HackTheBox yoki TryHackMe kabi platformalarda o‘z reytingingizni oshiring — bu sizning portfoliongiz uchun eng kuchli hujjat bo‘ladi!""",

        "ru": """Самые сильные гранты по кибербезопасности (Elite)

Эти университеты считаются «центром» кибербезопасности. Получить грант сложно, но диплом открывает двери по всему миру.

Carnegie Mellon University (CMU) — США

Тип гранта: CyberCorps: Scholarship for Service (SFS) и внутренняя финансовая помощь.

Особенность: Постоянно занимает 1-е место в мире по кибербезопасности. Имеет известный исследовательский центр CyLab.

Требования: Очень высокий академический уровень, логическое мышление и сильные знания программирования.

Tallinn University of Technology (TalTech) — Эстония

Тип гранта: Estonian Government Scholarship. Эстония — мировой лидер в кибербезопасности (здесь расположен центр НАТО).

Особенность: Магистратура по Cybersecurity полностью на английском языке, высокий шанс получить грант.

Требования: Диплом бакалавра в IT, IELTS 6.0+ и участие в CTF соревнованиях.

Университеты с более высокой вероятностью получения гранта:

University of Tartu — Эстония

Тип гранта: Tuition-Waiver Scholarship (полное покрытие обучения).

Особенность: Сильные программы по криптографии и безопасности электронного правительства.

Возможность: Для студентов из Узбекистана поступление и получение визы проще, чем во многих странах Европы.

TU Darmstadt — Германия

Тип гранта: DAAD или Deutschlandstipendium.

Обучение: В государственных вузах Германии почти бесплатное (небольшой семестровый взнос).

Особенность: Считается «столицей» кибербезопасности Германии. Здесь находится крупнейший исследовательский центр ATHENE.

Возможность: С немецким языком на уровне C1 шанс поступления очень высокий. На английские программы — IELTS 6.5+.

Итог:
В кибербезопасности одной теории недостаточно.
Развивайтесь на платформах HackTheBox и TryHackMe — это сильнейшая часть вашего портфолио.""",

        "en": """Top Cybersecurity Scholarships (Elite)

These universities are considered the global “centers” of cybersecurity. Getting a scholarship is difficult, but the diploma opens doors worldwide.

Carnegie Mellon University (CMU) — USA

Scholarship: CyberCorps: Scholarship for Service (SFS) and internal financial aid.

Highlight: Ranked #1 globally in cybersecurity. Home to the famous CyLab research center.

Requirements: Excellent academic performance, strong logic, and programming skills.

Tallinn University of Technology (TalTech) — Estonia

Scholarship: Estonian Government Scholarship. Estonia is a global leader in cybersecurity (NATO cyber center is located here).

Highlight: Cybersecurity Master’s program fully in English with high scholarship chances.

Requirements: Bachelor’s degree in IT, IELTS 6.0+, and CTF participation.

Universities with higher chances of full scholarships:

University of Tartu — Estonia

Scholarship: Tuition-Waiver (100% tuition coverage).

Highlight: Strong programs in cryptography and e-government security.

Opportunity: Easier admission and visa process compared to many European countries.

TU Darmstadt — Germany

Scholarship: DAAD or Deutschlandstipendium.

Tuition: Almost free (small semester fee).

Highlight: Known as Germany’s cybersecurity capital. Home to ATHENE research center.

Opportunity: German C1 → very high admission chance. English programs → IELTS 6.5+.

Conclusion:
In cybersecurity, theory alone is not enough.
Build your ranking on HackTheBox and TryHackMe — this is your strongest portfolio proof."""
    },
    "robot": {
        "uz": """​🤖 Robototexnika Bo‘yicha Eng Kuchli Grantlar (Elite)

​Bu yerda o‘qish sizni dunyoning eng yirik texnologik kompaniyalari (Tesla, Boston Dynamics, NASA) uchun tayyor kadrga aylantiradi.

​1. ETH Zurich — Shveysariya

​Grant turi: Excellence Scholarship & Opportunity Programme (ESOP). O‘qish bepul va yashash xarajatlarini to‘liq qoplaydigan stipendiya beriladi.

​Xususiyati: Robototexnika bo‘yicha Yevropaning #1 universiteti. Dunyoga mashhur "flying robots" (uchuvchi robotlar) aynan shu yerda rivojlantirilgan.

​Talablar: Bakalavrdan olingan a'lo baholar (GPA 4.8+) va kuchli ilmiy tadqiqot salohiyati.

​2. Nanyang Technological University (NTU) — Singapur

​Grant turi: Nanyang Scholarship. O‘qish to‘lovi, turar joy va oylik stipendiyani o‘z ichiga oladi.

​Xususiyati: Muhandislik va robototexnika sohasida Osiyoning eng ilg‘or laboratoriyalariga ega.

​Talablar: Matematika va Fizikadan mukammal bilim, IELTS 7.0+ va xalqaro robototexnika musobaqalaridagi ishtirok.

​✅ Grant Yutish Oson va 100% Imkoniyat Beruvchi OTMlar

​Ushbu universitetlarda texnik yo‘nalishlar uchun hukumat grantlari va ichki yordamlar juda keng ko‘lamda ajratiladi.

​1. Politecnico di Torino (PoliTo) — Italiya

​Grant turi: EDISU Piemonte Scholarship. Bu grant talabaning oilaviy daromadiga qarab beriladi va o‘qishni bepul qilish bilan birga, yashash uchun pul ham beradi.

​Xususiyati: Italiyadagi eng kuchli texnika universiteti. "Mechatronics Engineering" yo‘nalishi robototexnika uchun eng maqbul yo‘ldir.

​Imkoniyat: Italiyaga qabul qilinish uchun TIL (muhandislik testi) topshirish kifoya, ko'p hollarda grant olish jarayoni shaffof va oson.

​2. Czech Technical University (CTU) — Chexiya

​Grant turi: Government Scholarship va Erasmus+. Agar siz chex tilini o‘rgansangiz, ta’lim 100% bepul. Ingliz tilidagi dasturlar uchun ham ko‘plab stipendiyalar mavjud.

​Xususiyati: Markaziy Yevropadagi eng qadimgi va kuchli texnika universitetlaridan biri. Robototexnika va kiber-fizik tizimlar bo‘yicha juda kuchli maktabga ega.

​Imkoniyat: Chexiya talabalar uchun yashash xarajatlari arzonligi va o‘qishga kirish talablari (IELTS 6.0+) nisbatan soddaligi bilan ajralib turadi.
​
​"Robototexnik bo‘lish uchun faqat kitob o‘qish yetarli emas. Hozirdanoq Arduino yoki ROS (Robot Operating System) bilan amaliy loyihalar qilishni boshlang. Sizning qo'lingiz bilan yasalgan oddiy robot — mingta sertifikatdan kuchliroq dalil bo'ladi!""",

        "ru": """Самые сильные гранты по робототехнике (Elite)

Обучение здесь готовит вас к работе в крупнейших технологических компаниях мира (Tesla, Boston Dynamics, NASA).

ETH Zurich — Швейцария

Тип гранта: Excellence Scholarship & Opportunity Programme (ESOP). Полностью покрывает обучение и расходы на проживание.

Особенность: №1 в Европе по робототехнике. Именно здесь разработаны известные «летающие роботы».

Требования: Отличный GPA (4.8+), высокий научный потенциал.

Nanyang Technological University (NTU) — Сингапур

Тип гранта: Nanyang Scholarship (обучение, проживание и стипендия).

Особенность: Одна из самых передовых инженерных лабораторий в Азии.

Требования: Сильные знания математики и физики, IELTS 7.0+, участие в международных соревнованиях.

Университеты с более высокой вероятностью получения гранта:

Politecnico di Torino (PoliTo) — Италия

Тип гранта: EDISU Piemonte (бесплатное обучение + финансовая помощь на проживание).

Особенность: Один из лучших технических вузов Италии. Направление Mechatronics Engineering идеально для робототехники.

Возможность: Для поступления достаточно сдать TIL тест. Процесс получения гранта прозрачный.

Czech Technical University (CTU) — Чехия

Тип гранта: Government Scholarship и Erasmus+.

Обучение: Бесплатно при знании чешского языка, также есть стипендии на английские программы.

Особенность: Один из старейших технических вузов Европы с сильной школой робототехники и кибер-физических систем.

Возможность: Низкие расходы на жизнь и относительно простые требования (IELTS 6.0+).

Итог:
Чтобы стать робототехником, одной теории недостаточно.
Начните уже сейчас работать с Arduino или ROS.
Даже простой робот, сделанный своими руками, ценнее тысячи сертификатов.""",

        "en": """Top Robotics Scholarships (Elite)

Studying here prepares you for careers in top global tech companies (Tesla, Boston Dynamics, NASA).

ETH Zurich — Switzerland

Scholarship: Excellence Scholarship & Opportunity Programme (ESOP) (covers tuition and living expenses).

Highlight: #1 in Europe for robotics. Known for developing “flying robots.”

Requirements: Excellent GPA (4.8+), strong research potential.

Nanyang Technological University (NTU) — Singapore

Scholarship: Nanyang Scholarship (tuition, housing, stipend).

Highlight: One of Asia’s most advanced engineering labs.

Requirements: Strong math & physics, IELTS 7.0+, competition experience.

Universities with higher chances of full scholarships:

Politecnico di Torino (PoliTo) — Italy

Scholarship: EDISU Piemonte (free tuition + living support).

Highlight: Top technical university in Italy. Mechatronics Engineering is ideal for robotics.

Opportunity: Admission often requires only TIL test, scholarship process is transparent.

Czech Technical University (CTU) — Czech Republic

Scholarship: Government Scholarship and Erasmus+.

Tuition: Free in Czech language, scholarships available in English programs.

Highlight: One of Europe’s oldest and strongest technical universities in robotics and cyber-physical systems.

Opportunity: Low living costs and relatively easy requirements (IELTS 6.0+).

Conclusion:
To become a robotics engineer, theory alone is not enough.
Start building projects with Arduino or ROS now.
A simple robot you build yourself is stronger proof than thousands of certificates."""
    },
    "contact": {
        "uz": """📩 Biz bilan bog‘lanish
​Savollaringiz, takliflaringiz yoki hamkorlik loyihalaringiz bormi? Biz sizga yordam berishdan mamnunmiz!

​👨‍💻 Administrator bilan aloqa:

🌐 Telegram: [ @sdproject1 ]
📞 Telefon: [ +998990017899 ]

​Ish vaqti: 09:00 dan 18:00 gacha.

​Kelajagingizni biz bilan quring! 🚀""",

        "ru": """📩 Свяжитесь с нами

Есть вопросы, предложения или идеи для сотрудничества? Мы будем рады вам помочь!

👨‍💻 Связь с администратором:

🌐 Telegram: @sdproject1
📞 Телефон: +998990017899

⏰ Рабочее время: с 09:00 до 18:00

🚀 Стройте своё будущее вместе с нами!""",

        "en": """📩 Contact Us

Do you have questions, suggestions, or collaboration ideas? We are happy to help you!

👨‍💻 Contact the administrator:

🌐 Telegram: @sdproject1
📞 Phone: +998990017899

⏰ Working hours: 09:00 – 18:00

🚀 Build your future with us!"""
    }
}

# ====== KEYBOARDS ======
def lang_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇺🇿 O'zbek"), KeyboardButton(text="🇷🇺 Русский")],
            [KeyboardButton(text="🇬🇧 English")]
        ],
        resize_keyboard=True
    )

def main_kb(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=DATA[lang]["strategy"]), KeyboardButton(text=DATA[lang]["uni"])],
            [KeyboardButton(text=DATA[lang]["net"]), KeyboardButton(text=DATA[lang]["contact"])],
            [KeyboardButton(text=DATA[lang]["settings"])]
        ],
        resize_keyboard=True
    )

def back_kb(lang):
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=DATA[lang]["back"])]],
        resize_keyboard=True
    )

def directions_kb(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=DATA[lang]["ai"]), KeyboardButton(text=DATA[lang]["cyber"])],
            [KeyboardButton(text=DATA[lang]["robot"])],
            [KeyboardButton(text=DATA[lang]["back"])]
        ],
        resize_keyboard=True
    )

def net_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Telegram", url="https://t.me/techmind_uz_main")],
        [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/techmindknowledge?igsh=YXdjM2ZjNzlrZDFw")]
    ])

def sub_kb(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Kanal", url="https://t.me/techmind_uz_main")],
        [InlineKeyboardButton(text=DATA[lang]["check"], callback_data="check_sub")]
    ])

# ====== START ======
@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(DATA["uz"]["lang"], reply_markup=lang_kb())

# ====== LANGUAGE ======
@dp.message(F.text.in_(["🇺🇿 O'zbek", "🇷🇺 Русский", "🇬🇧 English"]))
async def set_lang(msg: Message):
    if "O'zbek" in msg.text:
        user_lang[msg.from_user.id] = "uz"
    elif "Рус" in msg.text:
        user_lang[msg.from_user.id] = "ru"
    else:
        user_lang[msg.from_user.id] = "en"

    lang = user_lang[msg.from_user.id]
    await msg.answer(DATA[lang]["main"], reply_markup=main_kb(lang))

# ====== STRATEGY ======
@dp.message(F.text.in_([DATA['uz']['strategy'], DATA['ru']['strategy'], DATA['en']['strategy']]))
async def strategy(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(DATA[lang]["subscribe"], reply_markup=sub_kb(lang))

@dp.callback_query(F.data == "check_sub")
async def check(call):
    user_id = call.from_user.id
    lang = user_lang.get(user_id, "uz")

    member = await bot.get_chat_member(CHANNEL, user_id)

    if member.status in ["member", "creator", "administrator"]:
        await call.message.answer(CONTENT["strategy"][lang], reply_markup=back_kb(lang))
    else:
        await call.answer(DATA[lang]["subscribe"], show_alert=True)

# ====== UNIVERSITIES ======
@dp.message(F.text.in_([DATA['uz']['uni'], DATA['ru']['uni'], DATA['en']['uni']]))
async def uni(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=DATA[lang]["directions"])],
            [KeyboardButton(text=DATA[lang]["back"])]
        ],
        resize_keyboard=True
    )
    await msg.answer(DATA[lang]["directions"], reply_markup=kb)

@dp.message(F.text.in_([DATA['uz']['directions'], DATA['ru']['directions'], DATA['en']['directions']]))
async def directions(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(DATA[lang]["directions"], reply_markup=directions_kb(lang))

# ====== AI / CYBER / ROBOT ======
@dp.message(F.text.in_([DATA['uz']['ai'], DATA['ru']['ai'], DATA['en']['ai']]))
async def ai(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(CONTENT["ai"][lang], reply_markup=back_kb(lang))

@dp.message(F.text.in_([DATA['uz']['cyber'], DATA['ru']['cyber'], DATA['en']['cyber']]))
async def cyber(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(CONTENT["cyber"][lang], reply_markup=back_kb(lang))

@dp.message(F.text.in_([DATA['uz']['robot'], DATA['ru']['robot'], DATA['en']['robot']]))
async def robot(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(CONTENT["robot"][lang], reply_markup=back_kb(lang))

# ====== NETWORK ======
@dp.message(F.text.in_([DATA['uz']['net'], DATA['ru']['net'], DATA['en']['net']]))
async def net(msg: Message):
    await msg.answer("🌐", reply_markup=net_kb())

# ====== CONTACT ======
@dp.message(F.text.in_([DATA['uz']['contact'], DATA['ru']['contact'], DATA['en']['contact']]))
async def contact(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(CONTENT["contact"][lang], reply_markup=back_kb(lang))

# ====== SETTINGS ======
@dp.message(F.text.in_([DATA['uz']['settings'], DATA['ru']['settings'], DATA['en']['settings']]))
async def settings(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=DATA[lang]["change_lang"])],
            [KeyboardButton(text=DATA[lang]["back"])]
        ],
        resize_keyboard=True
    )
    await msg.answer(DATA[lang]["settings"], reply_markup=kb)

@dp.message(F.text.in_([DATA['uz']['change_lang'], DATA['ru']['change_lang'], DATA['en']['change_lang']]))
async def change_lang(msg: Message):
    await msg.answer("🌐", reply_markup=lang_kb())

# ====== BACK ======
@dp.message(F.text.in_([DATA['uz']['back'], DATA['ru']['back'], DATA['en']['back']]))
async def back(msg: Message):
    lang = user_lang.get(msg.from_user.id, "uz")
    await msg.answer(DATA[lang]["main"], reply_markup=main_kb(lang))

# ====== RUN ======
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
