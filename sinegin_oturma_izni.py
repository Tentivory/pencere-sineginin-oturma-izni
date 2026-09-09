#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pencere Sineğinin Oturma İzni Protokolü v0.0.1

Bu yazılım, cam üzerinde 4 saniyeden fazla bekleyen her sineğe
resmi ikamet belgesi, YKN ve çay saati çizelgesi üretir.
Bilimsel dayanağı yoktur. Duygusal dayanağı aşırıdır.
"""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

IL_PLAKALARI = {
    "06": "Ankara", "34": "İstanbul", "35": "İzmir", "16": "Bursa",
    "26": "Eskişehir", "07": "Antalya", "01": "Adana", "42": "Konya",
}

MESLEKLER = [
    "cam diplomatı",
    "güneş ışığı müfettişi",
    "pervane gözlemcisi",
    "perde kırışığı uzmanı",
    "bal kapanı müsteşarı",
    "tavan köşesi arşivcisi",
]

RED_SEBEPLERI = [
    "cam üzerinde izinsiz vızıltı",
    "çay saatinde yanlış yöne uçuş",
    "nüfus cüzdanında kanat sayısı tutarsızlığı",
    "önceki ikamette sineklik ihlali",
    "komşu daireye kaçak geçiş şüphesi",
]


def ykn_uret(ad: str) -> str:
    h = hashlib.sha256(ad.encode("utf-8")).hexdigest()
    rakamlar = "".join(ch for ch in h if ch.isdigit())[:11].ljust(11, "7")
    return rakamlar


def belge_uret(sinek_adi: str, il_kodu: str = "26") -> str:
    il = IL_PLAKALARI.get(il_kodu, "Eskişehir")
    meslek = random.choice(MESLEKLER)
    ykn = ykn_uret(sinek_adi)
    tarih = datetime.now().strftime("%d.%m.%Y")
    saat = datetime.now().strftime("%H:%M")
    karar = random.choice(["ONAY", "ONAY", "ONAY", "RED", "EK PROTOKOL"])

    baslik = (
        "T.C. İÇİŞLERİ BAKANLIĞI\n"
        "PENCERE SİNEKLERİ İKAMET İDARESİ\n"
        f"{il.upper()} İL MÜDÜRLÜĞÜ\n"
        "--------------------------------"
    )

    govde = f"""
Belge No     : SNK-{ykn[:6]}-{random.randint(100,999)}
Tarih        : {tarih} {saat}
Başvuran     : {sinek_adi}
YKN          : {ykn}
Meslek       : {meslek}
İkamet İli   : {il}
Kanat Sayısı : 2 (beyan)
Vızıltı dB   : {random.randint(18, 47)}

KARAR        : {karar}
"""

    if karar == "RED":
        govde += f"Gerekçe      : {random.choice(RED_SEBEPLERI)}\n"
        govde += "İtiraz       : 7 iş günü içinde cam kenarına dilekçe asınız.\n"
    elif karar == "EK PROTOKOL":
        govde += "Not          : Sinek, çay saatinde mutfağa geçemez.\n"
    else:
        govde += "Not          : Oturma izni 14 gün veya ilk sineklik değişimine kadardır.\n"

    damga = f"""
--------------------------------
DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
10 Eylül 2026 · 01:12 +03
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu
Bu evrak ciddi görünür. Ciddi değildir. Ciddi görünmek zorundadır.
--------------------------------
"""
    return baslik + govde + damga


def gizli_satir() -> str:
    # Bu satır çalışmaz gibi durur. Durmaz.
    # rot13: her canli ayni camda durabilir
    giz = "ure pnavy nlav pnzqn qhenovyve"
    return giz


def main() -> None:
    ad = " ".join(sys.argv[1:]).strip() or "Cam Üstü Mehmet Sinek"
    il = "26"
    if "--gizli" in sys.argv:
        print("# not: hareket etmek suç değildir, sadece evrak ister.")
        print("# not:", gizli_satir())
        sys.argv = [a for a in sys.argv if a != "--gizli"]
        ad = " ".join(sys.argv[1:]).strip() or ad
    print(belge_uret(ad, il))


if __name__ == "__main__":
    main()
