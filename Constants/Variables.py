def init():
    global lessons_list, words_list, descriptions, double_lessons, is_first_scraping

    lessons_list = []
    words_list = []
    is_first_scraping = True
    descriptions = {
        "colours": "Naucz się podstawowych kolorów w języku angielskim. Od czerwonego do fioletowego, gdy nauczysz się tej lekcji już żadna tęcza nie będzie Ci straszna.",
        "everyday objects": "W tej lekcji poznasz przedmioty codziennego użytku. Dzięki tej wiedzy dowiesz się m.in. jak poradzić sobie, gdy będąc na wycieczce w Anglii zgubisz okulary lub laptopa.",
        "actions": "Jak w języku angielskim nazywają się podstawowe czynności? Jeśli zastanawiasz się jak to jest czytać lub pisać (po angielsku), to ta lekcja jest właśnie dla Ciebie.",
        "food and drinks": "Boisz się sytuacji, w której w angielskim sklepie lub restauracji nie będziesz znał nazw jedzenia czy napoi? W tej lekcji poznasz najważniejsze pojęcia związane z żywnością.",
        "weather": "Stereotypowo przyjęło się, że Anglicy w każdej sytuacji towarzyskiej rozmawiają o pogodzie. Oczywiście nikt nie chciałby poczuć się wykluczony w takiej sytuacji, dlatego w tej lekcji dowiesz się o angielskich wyrażeniach pogodowych.",
        "body parts": "Boli Cię głowa i potrzebujesz tabletki? A może osoba obok Ciebie ma rozmazaną szminkę i chcesz ją o tym poinformować? Z tą lekcją nauczysz się nazw najważniejszych części ciała.",
        "clothes": "Jesteś w sklepie i szukasz czerwonej koszulki, a nie wiesz jak zapytać o to sprzedawczynię? Kolory już poznałeś w pierwszej lekcji, a więc teraz czas na ubrania. Od kapelusza do butów, w tej lekcji nauczysz się części stroju.",
        "home": "Dowiedz się, jak po angielsku nazywają się pokoje oraz meble w domu. Tą wiedzę możesz wykorzystać podczas opowiadania o swoim miejscu zamieszkania i przedmiotach, które się w nim znajdują.",
        "jobs": "Potrzebujesz zawołać lekarza lub policjanta w sytuacji krytycznej? A może chcesz powiedzieć jaki zawód wykonujesz? W tej lekcji poznasz najważniejsze zawody w języku angielskim.",
        "transport": "Gdy podróżujesz po mieście, bardzo ważnym elementem są środki transportu. Przydatna jest więc umiejętność rozróżnienia, który rozkład jazdy jest dla pociągu, a który dla autobusu. W tej lekcji poznasz słownictwo dotyczące podstawowych środków komunikacji.",
        "animals": "Nie wiesz jak powiedzieć o swoim ukochanym zwierzaku? Dzięki tej lekcji poznasz nazwy zwierząt po angielsku, a także będziesz mógł odnaleźć się w angielskim zoo.",
        "nature": "Czy kiedyś udałeś się na piękny spacer po górach i zastanawiałeś się, jak po angielsku nazywają się przydrożne drzewa, jeziora czy krzaki? W tej lekcji poszerzysz swoje słownictwo o pojęcia związane z naturą.",
        "holidays": "W tej kategorii znajdziesz wszystkie niezbędne słowa nt. podróży i wakacji. Gdy szukasz hotelu lub pola namiotowego, ucząc się tych wyrażeń, łatwiej będzie Ci odnaleźć się na wycieczce za granicą.",
        "bedroom": "Jesteś w domu handlowym i nie wiesz, jak po angielsku nazwać znajdujące się tam meble? Dzięki tej lekcji poznasz nazwy przedmiotów i mebli, które znajdują się w każdej sypialni.",
        "in a town": "Czy wędrując po mieście i patrząc na budynki wokół, zastanawiałeś się - jak te miejsca nazywają się w języku angielskim? Jeśli odpowiedź to tak, ta lekcja jest stworzona dla Ciebie.",
        "physical activity": "Jeśli zastanawiasz się, w jaki sposób powiedzieć, że chcesz iść popływać czy pojeździć na rowerze lub deskorolce, ta lekcja jest właśnie dla Ciebie. Poznaj podstawowe słowa wyrażające aktywność fizyczną.",
        "living room": "W tej lekcji poznasz nazwy przedmiotów znajdujących się w każdym salonie. Nieważne czy to telewizor czy kanapa, teraz będąc w sklepie meblowym, będziesz znał każdy angielski odpowiednik produktów.",
        "bathroom": "Potrzebujesz kupić szampon do włosów lub mydło, gdy jesteś za granicą? A może szukasz w sklepie meblowym sekcji dotyczącej łazienek? W tej kategorii poznasz angielskie nazwy przedmiotów i mebli znajdujących się w łazience.",
        "school": "W tej lekcji dowiesz się, jak nazywają się elementy wyposażenia każdej szkoły. Nauczysz się też najważniejszych przedmiotów szkolnych. Nieważne, czy Twoim ulubionym przedmiotem jest matematyka, czy język polski, teraz poznasz ich angielskie odpowiedniki!",
        "health": "Jesteś za granicą i potrzebujesz pomocy lekarza? Lub próbujesz zakomunikować, jakiego rodzaju ból Ci doskwiera? W tej kategorii poznasz najważniejsze słownictwo dotyczące zdrowia.",
        "restaurant": "Czy będąc w restauracji zastanawiasz się, jak po angielsku nazywają się sztućce i naczynia, których używasz? A może nie wiesz, jak zawołać kelnera? Dzięki tej lekcji poznasz słownictwo używane w restauracjach."
    }

    double_lessons = {
        "food": "food and drinks", 
        "drinks": "food and drinks", 
        "room": "home", 
        "garden": "home", 
        "money": "everyday objects"
    }



    