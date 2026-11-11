# -*- coding: utf-8 -*-
# Bonnie ve Clyde (1934) – senaryo taslağı. Yeni plan: uzun video ~4.500 karakter + 6 Short.
# Kaynaklar: PBS American Experience "Bonnie & Clyde"; FBI Famous Cases; Wikimedia Commons fotoğraf kayıtları.
SECTIONS = [
("giris",
 "Bu fotoğraflar, yayımlanmak için çekilmedi. "
 "Bin dokuz yüz otuz üç baharında bir çete, polis baskınından kaçarken arkasında banyo edilmemiş film ruloları bıraktı. "
 "Polis filmleri banyo ettirdi. Ve Amerika, aradığı iki kişinin yüzünü ilk kez gördü: gülen, silahlarla poz veren, birbirine sarılan iki genç. "
 "Bu, Bonnie ve Clyde'ın hikâyesi. Ve bu videodaki fotoğrafların birçoğunu onlar kendi çekti."),
("tanisma",
 "Clyde Barrow, bin dokuz yüz dokuzda Teksas'ta yoksul bir çiftçi ailesinde doğdu. "
 "Bonnie Parker ondan bir yaş küçüktü. Okulda başarılı bir öğrenciydi, şiir yazardı. On beş yaşında evlendi, evliliği yürümedi. "
 "Ocak bin dokuz yüz otuzda Dallas'ta tanıştılar. Bonnie on dokuz, Clyde yirmi yaşındaydı. "
 "Birkaç hafta sonra Clyde tutuklandı."),
("hapishane",
 "Clyde, Teksas'ın en sert cezaevlerinden biri olan Eastham hapishane çiftliğine gönderildi. Orada yaşadıkları onu değiştirdi. "
 "Tarlada çalışmaktan kurtulmak için ayağının iki parmağını kestirdi. "
 "Oysa annesi çoktan af için başvurmuştu. Clyde kısa süre sonra, Şubat bin dokuz yüz otuz ikide serbest bırakıldı. "
 "Dışarı çıktığında aklında tek bir şey vardı: bir gün Eastham'a geri dönmek."),
("soygunlar",
 "Filmlerin anlattığının aksine, Bonnie ve Clyde büyük banka soyguncuları değildi. "
 "Çoğu zaman benzin istasyonlarını ve küçük dükkânları soydular. Bazen ellerine yalnızca birkaç dolar geçti. "
 "Amerika, Büyük Buhran'ın ortasındaydı. Bankalar insanların evlerine el koyarken, gazeteler bu genç çifti neredeyse kahraman gibi yazdı. "
 "Ama gerçek farklıydı. Çetenin, dokuzu polis olmak üzere en az on üç kişinin ölümünden sorumlu olduğuna inanılıyor."),
("joplin",
 "Nisan bin dokuz yüz otuz üç. Çete, Missouri'nin Joplin kentinde bir garajın üstündeki daireye yerleşti. "
 "Yanlarında Clyde'ın ağabeyi Buck, Buck'ın eşi Blanche ve genç W. D. Jones vardı. Komşular şüphelendi. "
 "On üç Nisan'da polis kapıya geldi. Çıkan çatışmada iki polis hayatını kaybetti, çete kaçtı. "
 "Geride silahlar, Bonnie'nin yazdığı bir şiir ve o film ruloları kaldı. "
 "İki gün sonra fotoğraflar gazetenin ilk sayfasındaydı. "
 "Bonnie'nin ağzında puroyla, elinde tabancayla verdiği poz bütün ülkeye yayıldı. "
 "Oysa o kare bir şakaydı. Ve o şaka, Bonnie'yi Amerika'nın en tanınan kadın suçlusu yaptı."),
("kacis",
 "Şöhret, kaçmayı zorlaştırdı. Artık herkes yüzlerini tanıyordu. Otellerde kalamadılar. Arabada uyudular, derelerde yıkandılar. "
 "Haziran bin dokuz yüz otuz üçte Clyde, Teksas'ta yoldaki bir uyarı işaretini fark etmedi. Araba devrildi ve alev aldı. "
 "Bonnie'nin bacağı ağır biçimde yandı. O günden sonra zor yürüdü; çoğu zaman Clyde onu kucağında taşıdı. "
 "Temmuz ayında Missouri'de bir motelde kuşatıldılar. Buck başından vuruldu. "
 "Dört gün sonra Iowa'da yeniden sarıldılar. Clyde, Bonnie'yi kurtarmak için ağabeyini geride bırakmak zorunda kaldı. "
 "Buck birkaç gün sonra öldü. Blanche hapse girdi."),
("hamer",
 "Ocak bin dokuz yüz otuz dört. Clyde yıllardır beklediği şeyi yaptı. Eastham hapishane çiftliğine baskın düzenledi ve beş mahkûmu kaçırdı. "
 "Bu, Teksas için bardağı taşıran damla oldu. Cezaevleri müdürü, eski Teksas korucusu Frank Hamer'ı göreve çağırdı. "
 "Hamer'ın tek bir işi vardı: Bonnie ve Clyde'ı bulmak. "
 "Aylarca izlerini sürdü ve bir düzen fark etti. Çift nereye kaçarsa kaçsın, sonunda hep ailelerini görmeye dönüyordu. "
 "Kaçırılan mahkûmlardan Henry Methvin'in ailesi Louisiana'da yaşıyordu. "
 "Hamer, Methvin ailesiyle anlaştı: oğullarına af karşılığında, çiftin geçeceği yolu söyleyeceklerdi."),
("siir",
 "Bonnie, sonun yaklaştığını biliyordu. Ölümünden haftalar önce annesine bir şiir verdi. "
 "Şiirde kendi hikâyelerini anlatıyor ve nasıl biteceğini yazıyordu: bir gün birlikte vurulacak ve yan yana gömüleceklerdi."),
("pusu",
 "Yirmi üç Mayıs bin dokuz yüz otuz dört. Louisiana'da, Gibsland kasabası yakınlarında bir orman yolu. "
 "Altı polis, çalıların arasında saatlerdir bekliyordu. "
 "Yolun kenarında Methvin'in babası, kamyoneti bozulmuş gibi duruyordu. "
 "Sabah dokuzu çeyrek geçe bir Ford V sekiz yaklaştı. Clyde, tanıdığı kamyoneti görünce yavaşladı. "
 "Polisler ateş açtı. Her şey saniyeler içinde bitti. Arabaya yüz elliden fazla kurşun isabet etti. "
 "Bonnie yirmi üç, Clyde yirmi beş yaşındaydı."),
("kapanis",
 "Haber birkaç saat içinde bütün ülkeye yayıldı. Dallas'ta iki cenaze evinin önünde günlerce kuyruk oluştu. "
 "Gazeteler iki günde yaklaşık yarım milyon ek baskı sattı. "
 "Bonnie'nin şiirindeki son dilek ise gerçekleşmedi. Annesi buna izin vermedi. Bonnie ve Clyde, Dallas'ta iki ayrı mezarlığa gömüldü. "
 "Geriye o fotoğraflar kaldı: şaka olsun diye çekilen ve iki genci efsaneye çeviren kareler. "
 "Sizce o film ruloları hiç bulunmasaydı, Bonnie ve Clyde'ı bugün hatırlar mıydık? Yorumlarda yazın."),
]

# Shorts: (anahtar, YouTube başlığı, metin). Kural: somut nesne/rakam çelişkisiyle açılır,
# "Tüm hikâye kanalımızda" yok, soru ya da ilk cümleye dönen cümleyle biter.
SHORTS = [
("short1_puro", "Şaka Olsun Diye Çekildi, Bütün Amerika Onu Bu Fotoğrafla Tanıdı 📷 Bonnie ve Clyde",
 "Bu fotoğraf bir şakaydı. Ama Bonnie Parker'ı Amerika'nın en tanınan kadın suçlusu yaptı. "
 "Bin dokuz yüz otuz üçte çete, polis baskınından kaçarken arkasında film ruloları bıraktı. "
 "Polis filmleri banyo ettirdi. İki gün sonra bu kare gazetelerin ilk sayfasındaydı. "
 "Ağzında puro, elinde tabanca. Kimse bunun bir şaka olduğunu bilmiyordu."),
("short2_parmak", "Hapisten Kurtulmak İçin Parmaklarını Kestirdi, Günler Sonra Affedildi 😶 Clyde Barrow",
 "Clyde Barrow, hapishanede çalışmaktan kurtulmak için ayağının iki parmağını kestirdi. Kısa süre sonra zaten serbest bırakılacaktı. "
 "Teksas'taki Eastham hapishane çiftliğinde tarlada çalışmaya dayanamadı. "
 "Oysa annesi çoktan af için başvurmuştu. "
 "Clyde hayatının sonuna kadar aksayarak yürüdü. Boşuna verilmiş iki parmak yüzünden."),
("short3_birkac_dolar", "Efsane Soyguncuların Eline Bazen Birkaç Dolar Geçti 💵 Bonnie ve Clyde",
 "Tarihin en ünlü soyguncu çiftinin eline, bazı soygunlarda yalnızca birkaç dolar geçti. "
 "Filmler onları büyük banka soyguncusu gibi gösterir. "
 "Gerçekte çoğu zaman benzin istasyonlarını ve küçük dükkânları soydular. Arabada uyudular, derelerde yıkandılar. "
 "Peki onları efsane yapan neydi: soygunlar mı, yoksa kendi çektikleri fotoğraflar mı?"),
("short4_siir", "Nasıl Öleceğini Şiirinde Yazdı, Haftalar Sonra Öyle Öldü ✍️ Bonnie Parker",
 "Bonnie Parker, nasıl öleceğini bir şiirde yazdı. Haftalar sonra tam öyle öldü. "
 "Şiiri annesine kendi eliyle verdi. İki şey yazmıştı: Clyde'la birlikte vurulacak ve yan yana gömüleceklerdi. "
 "Yirmi üç Mayıs bin dokuz yüz otuz dörtte birincisi gerçek oldu. "
 "İkincisi olmadı. Annesi izin vermedi; iki ayrı mezarlığa gömüldüler."),
("short5_kamyonet", "Yol Kenarındaki Bozuk Kamyonet Bir Tuzaktı 🚚 Bonnie ve Clyde 1934",
 "Yol kenarında bozulmuş bir kamyonet duruyordu. O kamyonet bir tuzaktı. "
 "Yirmi üç Mayıs bin dokuz yüz otuz dört, Louisiana. Altı polis çalıların arasında saatlerdir bekliyordu. "
 "Kamyonet, çetedeki bir arkadaşlarının babasına aitti. Clyde onu tanıdı ve yavaşladı. "
 "Her şey saniyeler içinde bitti. Onları ele veren, güvendikleri bir aileydi."),
("short6_araba", "Bu Arabada 150'den Fazla Kurşun İzi Var ve Hâlâ Sergileniyor 🚗 Bonnie ve Clyde",
 "Bu arabaya yüz elliden fazla kurşun isabet etti. Ve araba bugün hâlâ sergileniyor. "
 "Bin dokuz yüz otuz dört model bir Ford V sekiz. Clyde onu Kansas'ta bir aileden çalmıştı. "
 "Pusudan sonra araba yıllarca panayırlarda dolaştırıldı; insanlar görmek için para ödedi. "
 "Bugün Amerika'da, Nevada'da sergileniyor. Aradan doksan yıldan fazla geçti; kurşun izleri hâlâ yerinde."),
]

if __name__ == "__main__":
    t = " ".join(x for _, x in SECTIONS)
    print("uzun:", len(t), "karakter")
    tot = 0
    for k, _, s in SHORTS:
        print(k, len(s)); tot += len(s)
    print("shorts toplam:", tot, "| genel toplam:", len(t) + tot)
