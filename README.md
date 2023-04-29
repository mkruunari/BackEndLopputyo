# BackEndLopputyo

Tämä on PelaajaApi, jossa pystytään seuraamaan pelaajan edistystä ja lisäämään pelaajia ja luomaan niille eventtejä, ja myös hakemaan kaikki pelaajat ja tarkemmat tiedot heidän id:n perusteella

Myöskin eventtien haku onnistuu.

Voit ladata tämän API:n ZIP-tiedostona tai kirjoittamalla komentokehotteeseesi seuraavaa:

git clone https://github.com/mkruunari/BackEndLopputyo.git

Laita venv päälle komentokehotteesta, tai VsCodesta.

Kun venv on päällä, laita komentokehotteeseen:


pip install uvicorn fastapi requests

-->

uvicorn app.main:app --reload

Tämän jälkeen tulee näkyviin selainlinkki, mene osoitteeseen ja laita osoitteen perään /docs jossa pääset hallinnoimaan PelaajaAPI:a






