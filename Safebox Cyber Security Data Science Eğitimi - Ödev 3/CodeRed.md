# CodeRed 
2001 yılında ortaya çıkan ve Microsoft Internet Information Services (IIS) web sunucusunu hedef alan bir solucan virüstür. Hedef sistemdeki güvenlik açıklarını kullanarak yayılır ve etkilenen sistemleri istismar eder.

CodeRed virüsü, saldırılarının yoğunluğu ve yayılma hızı nedeniyle dikkat çekmiştir. Bu saldırı, internetin erken dönemlerinde büyük bir etki yaratmış ve güvenlik açıklarının önemi konusunda farkındalık oluşturmuştur. Virüsün ortaya çıkmasıyla birlikte, sistem yöneticileri ve güvenlik uzmanları güvenlik önlemlerini artırmak ve güncellemeleri takip etmek konusunda daha bilinçli hale gelmiştir.

---

Yayılma Yöntemi: CodeRed, hedef sistemlerdeki IIS sunucusunun "Indexing Service" bileşeninde bulunan bir güvenlik açığından yararlanır. Bu açık, sunucunun açık HTTP bağlantıları üzerinden kötü amaçlı kodu sisteme enjekte etmesine olanak tanır. Virüs, hedeflenen sunucuya özel olarak oluşturulan bir HTTP isteği göndererek yayılımını gerçekleştirir.

---
Yayılma Hızı: CodeRed, saldırıya uğrayan sistemler üzerinde hızla yayılabilir. Virüs, bir kez etkili bir sunucuya bulaştığında, yeni hedefler bulmak için rastgele IP adresleri oluşturur ve yayılma sürecini otomatik olarak devam ettirir.

---
Etkileri: CodeRed, enfekte ettiği sistemlerde ciddi etkilere neden olabilir. Virüs, hedef sunucunun belleğini aşırı yükleyebilir ve sistemi yavaşlatabilir. Ayrıca, virüsün saldırı gerçekleştirdiği sunucularda web sayfalarının erişilemez hale gelmesine neden olabilir.

---
Güvenlik Yaması: Microsoft, CodeRed salgınından sonra IIS sunucusundaki güvenlik açıklarını gidermek için bir güvenlik yaması yayınladı. Bu yama, sistem yöneticilerine saldırıya karşı korunmak için sunucularını güncellemelerini sağladı.

---
Code Red'in Davranış Kodu Red, sunucuya TCP bağlantı noktası 80 aracılığıyla bir GET /default.ida isteği gönderir. Kod, Microsoft'un dizin oluşturma yazılımı Internet Information Server'daki (IIS) arabellek taşması güvenlik açığından yararlanmak için yazılmıştır. Sonuç olarak, kod IIS sunucusu içinde çalışacaktır. Solucan virüsü tamamen bellekte çalışır ve sabit sürücüde algılanamaz. 3.569 bayt boyutundadır.Solucanın yükü, virüslü web sitesinin görüntülenmesi için bozulmalarını içerir:

### MERHABA! http://www.worm.com/welcome.html Çince hacklendi!


