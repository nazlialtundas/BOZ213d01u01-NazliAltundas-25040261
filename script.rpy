
define c = Character("Chiikawa", who_color="#F5A6C8")
define h = Character("Hachiware", who_color="#78C8F0")
define p = Character("[isim]", who_color="#100f0f")

label start:
    play music "audio/bgm.mp3.mpeg"

    $ isim = renpy.input("Adın ne?")
    $ isim = isim.strip()

    scene land
    with fade

    play sound "audio/cupapa.mp3.mpeg"
    show cslm at left
    c "Yaya! Upapa!"
    
    show hslm at right
    play sound "audio/hgunaydin.mp3.mpeg"
    h "Merhaba! Senin adın ne?"

    p "Ben [isim]."
    
    h "Tanıştığımıza memnun olduk!"

    c "Uwa uu uwa!"

    p "Bugün ne yapıyorsunuz?"

    hide hslm
    show hyat at right
    hide cslm
    show cyat at left
    h "Ormana gidiyoruz. Sen de gelsene!"
    hide hyat
    hide cyat

    menu:
        "Onlarla git":
            jump forest

        "Gitme":
            p "Bugün gelemem."
            
            show hyat2 at left
            show cagla at right
            play sound "audio/hbyby.mp3.mpeg"
            h "Tamam, başka zaman görüşürüz!"

            return


label forest:

    scene forest
    with fade

    show hmutlu at left
    show cmutlu at right
    h "İşte geldik!"

    play sound "audio/uwauwa.mp3.mpeg"
    c "Uu u wa wa uwa!"
    
    hide cmutlu
    show cslm at right
    p "Burası çok güzelmiş."

    hide hmutlu
    show hslm at left
    h "Birlikte dolaşalım mı?"

    p "Olur!"

    "Chiikawa, Hachiware ve [isim] ormanda yürümeye başladılar."
    hide cslm
    hide hslm

    scene black
    with fade

    stop music fadeout 2.0

    "Bugün Chiikawa ve Hachiware ile güzel bir gün geçirdin."

    "Belki de bu, yeni maceraların sadece başlangıcıdır..."

    pause 2.0

    centered "SON"

    pause 3.0

    return