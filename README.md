Bioinformatics Scripts
==================

###ortho_end_to_fasta.py

This script parses FastOrtho output and creates fasta files containing all sequences for each ortholog

Input:
```
ORTHOMCL25 (14 genes,6 taxa):    cds.comp8678_c0_seq2|m.1387(Daxi_longest.fasta.transdecoder) cds.comp7262_c0_seq2|m.1956(Plob_longest.fasta.transdecoder) cds.comp73244_c0_seq1|m.24467(Tcoc_longest.fasta.transdecoder)
```

Output: 
```
>Daxi|comp8678_c0_seq2_m.1387
AAACCAGCAAGTGCATTTCCAGAACTTGAAAATCTCAGTCTAGAAGAGCTCAAGCATCTTAATGATAAGCCTGAAGTTATGGATACTTTAGTAACAAAAGTAGATTCGGTTAAAAAAGTAGAAGCTGAAAAAGAAGAAGT
>Plob|cds.comp7262_c0_seq2_m.1956
AATCATAGATGTAAAAGGTCTGGCCATTTTGACTTCTTGTACCATGTATGTCCTAACATTACAGTCATGTTTTGTGTTTATCTTTTCAGAACCTTACCACCACAGTTTCCAAATGAAAGACCCCTTGTCAAGGTTGCTCC
>Tcoc|cds.comp73244_c0_seq1_m.24467
TTTCCAAGTGAGAGACCGATTGTGAAGGTGGCTCCACCCTTGGTACACCAATGGGTGAATGACCAGATGGTGGTTGTGGGCTGTCCTGCAATTAATAGTTTTTACATGCACTCTAATCTGGGTAGAGCCATTGTGGATGT
```

###ortho_filtering.py

This script searches FastOrtho output for orthologs matching the minimum required taxa from two user-defined lists

Ex. when seaching for orthologs matching two clades, or having at least one representative from each clade

Outputs a filtered .end file

Input:
```
ORTHOMCL0 (31 genes,2 taxa):     cds.comp98710_c0_seq1|m.34175(Tcoc_longest.fasta.transdecoder) cds.comp70288_c0_seq2|m.21967(Tcoc_longest.fasta.transdecoder) cds.comp82535_c0_seq1|m.30714(Tcoc_longest.fasta.transdecoder) cds.comp46143_c0_seq1|m.9426(Tcoc_longest.fasta.transdecoder) cds.comp130509_c0_seq1|m.38270(Tcoc_longest.fasta.transdecoder) cds.comp76493_c0_seq4|m.27865(Tcoc_longest.fasta.transdecoder) cds.comp82592_c0_seq1|m.30728(Tcoc_longest.fasta.transdecoder) cds.comp77455_c0_seq3|m.28969(Tcoc_longest.fasta.transdecoder) cds.comp77440_c0_seq1|m.28948(Tcoc_longest.fasta.transdecoder) cds.comp69534_c0_seq1|m.21350(Tcoc_longest.fasta.transdecoder) cds.comp54654_c0_seq1|m.12607(Tcoc_longest.fasta.transdecoder) cds.comp70609_c0_seq2|m.22222(Tcoc_longest.fasta.transdecoder) cds.comp23289_c0_seq1|m.3850(Tcoc_longest.fasta.transdecoder) cds.comp76005_c0_seq2|m.27342(Tcoc_longest.fasta.transdecoder) cds.comp121090_c0_seq1|m.37302(Tcoc_longest.fasta.transdecoder) cds.comp554_c0_seq1|m.55(Tcoc_longest.fasta.transdecoder) cds.comp71170_c0_seq1|m.22667(Tcoc_longest.fasta.transdecoder) cds.comp88411_c0_seq1|m.32111(Tcoc_longest.fasta.transdecoder) cds.comp76884_c0_seq13|m.28306(Tcoc_longest.fasta.transdecoder) cds.comp83778_c0_seq1|m.31006(Tcoc_longest.fasta.transdecoder) cds.comp29598_c0_seq1|m.5222(Tcoc_longest.fasta.transdecoder) cds.comp37242_c0_seq1|m.6928(Tcoc_longest.fasta.transdecoder) cds.comp33686_c0_seq1|m.6144(Tcoc_longest.fasta.transdecoder) cds.comp22327_c0_seq1|m.3663(Tcoc_longest.fasta.transdecoder) cds.comp49113_c0_seq3|m.10386(Tcoc_longest.fasta.transdecoder) cds.comp17904_c0_seq1|m.2796(Tcoc_longest.fasta.transdecoder) cds.comp30771_c0_seq1|m.5490(Tcoc_longest.fasta.transdecoder) cds.comp59990_c0_seq1|m.15291(Tcoc_longest.fasta.transdecoder) cds.comp56463_c0_seq1|m.13485(Tcoc_longest.fasta.transdecoder) cds.comp36471_c0_seq1|m.7480(Tmic_longest.fasta.transdecoder) cds.comp8401_c0_seq1|m.1721(Tmic_longest.fasta.transdecoder)
ORTHOMCL1 (29 genes,2 taxa):     cds.comp62860_c0_seq2|m.16839(Tcoc_longest.fasta.transdecoder) cds.comp16058_c0_seq1|m.2281(Tcoc_longest.fasta.transdecoder) cds.comp64781_c0_seq2|m.18056(Tcoc_longest.fasta.transdecoder) cds.comp109280_c0_seq1|m.35842(Tcoc_longest.fasta.transdecoder) cds.comp87722_c0_seq1|m.31939(Tcoc_longest.fasta.transdecoder) cds.comp36028_c0_seq1|m.6658(Tcoc_longest.fasta.transdecoder) cds.comp97625_c0_seq1|m.33959(Tcoc_longest.fasta.transdecoder) cds.comp83327_c0_seq1|m.30899(Tcoc_longest.fasta.transdecoder) cds.comp72321_c0_seq1|m.23670(Tcoc_longest.fasta.transdecoder) cds.comp76951_c0_seq5|m.28387(Tcoc_longest.fasta.transdecoder) cds.comp83968_c0_seq1|m.31058(Tcoc_longest.fasta.transdecoder) cds.comp30639_c0_seq1|m.5457(Tcoc_longest.fasta.transdecoder) cds.comp79912_c0_seq1|m.30091(Tcoc_longest.fasta.transdecoder) cds.comp57590_c0_seq2|m.14098(Tcoc_longest.fasta.transdecoder) cds.comp69593_c0_seq1|m.21399(Tcoc_longest.fasta.transdecoder) cds.comp87436_c0_seq1|m.31885(Tcoc_longest.fasta.transdecoder) cds.comp61085_c0_seq1|m.15850(Tcoc_longest.fasta.transdecoder) cds.comp117497_c0_seq1|m.36940(Tcoc_longest.fasta.transdecoder) cds.comp150548_c0_seq1|m.39660(Tcoc_longest.fasta.transdecoder) cds.comp34832_c0_seq1|m.6359(Tcoc_longest.fasta.transdecoder) cds.comp35232_c0_seq1|m.6451(Tcoc_longest.fasta.transdecoder) cds.comp35068_c0_seq1|m.6415(Tcoc_longest.fasta.transdecoder) cds.comp15664_c0_seq2|m.2122(Tcoc_longest.fasta.transdecoder) cds.comp57713_c0_seq1|m.14165(Tcoc_longest.fasta.transdecoder) cds.comp13628_c0_seq1|m.1607(Tcoc_longest.fasta.transdecoder) cds.comp65168_c0_seq1|m.18303(Tcoc_longest.fasta.transdecoder) cds.comp122812_c0_seq1|m.37532(Tcoc_longest.fasta.transdecoder) cds.comp31927_c0_seq1|m.5765(Tcoc_longest.fasta.transdecoder) cds.comp40864_c0_seq1|m.7847(Tmic_longest.fasta.transdecoder)
ORTHOMCL2 (27 genes,3 taxa):     cds.comp10393_c0_seq1|m.3165(Peve_longest.fasta.transdecoder) cds.comp6595_c0_seq1|m.2239(Peve_longest.fasta.transdecoder) cds.comp36885_c0_seq1|m.6851(Tcoc_longest.fasta.transdecoder) cds.comp74725_c0_seq1|m.25969(Tcoc_longest.fasta.transdecoder) cds.comp141416_c0_seq1|m.39107(Tcoc_longest.fasta.transdecoder) cds.comp69709_c0_seq1|m.21486(Tcoc_longest.fasta.transdecoder) cds.comp76495_c0_seq2|m.27868(Tcoc_longest.fasta.transdecoder) cds.comp69963_c0_seq1|m.21698(Tcoc_longest.fasta.transdecoder) cds.comp47627_c0_seq1|m.9923(Tcoc_longest.fasta.transdecoder) cds.comp74030_c0_seq6|m.25245(Tcoc_longest.fasta.transdecoder) cds.comp63354_c0_seq2|m.17149(Tcoc_longest.fasta.transdecoder) cds.comp23505_c0_seq2|m.3897(Tcoc_longest.fasta.transdecoder) cds.comp76754_c0_seq3|m.28166(Tcoc_longest.fasta.transdecoder) cds.comp3507_c0_seq1|m.374(Tcoc_longest.fasta.transdecoder) cds.comp64782_c0_seq1|m.18057(Tcoc_longest.fasta.transdecoder) cds.comp67084_c0_seq1|m.19566(Tcoc_longest.fasta.transdecoder) cds.comp47315_c0_seq1|m.9828(Tcoc_longest.fasta.transdecoder) cds.comp55427_c0_seq1|m.12964(Tcoc_longest.fasta.transdecoder) cds.comp128947_c0_seq1|m.38140(Tcoc_longest.fasta.transdecoder) cds.comp41720_c0_seq1|m.7923(Tcoc_longest.fasta.transdecoder) cds.comp65361_c0_seq1|m.18425(Tcoc_longest.fasta.transdecoder) cds.comp50990_c0_seq2|m.11021(Tcoc_longest.fasta.transdecoder) cds.comp59459_c0_seq2|m.15050(Tcoc_longest.fasta.transdecoder) cds.comp36601_c0_seq1|m.6788(Tcoc_longest.fasta.transdecoder) cds.comp142316_c0_seq1|m.39160(Tcoc_longest.fasta.transdecoder) cds.comp33615_c0_seq1|m.7191(Tmic_longest.fasta.transdecoder) cds.comp42960_c0_seq1|m.8019(Tmic_longest.fasta.transdecoder)
ORTHOMCL3 (22 genes,4 taxa):     cds.comp18812_c0_seq1|m.4422(Peve_longest.fasta.transdecoder) cds.comp20487_c0_seq1|m.6456(Plob_longest.fasta.transdecoder) cds.comp101181_c0_seq1|m.34582(Tcoc_longest.fasta.transdecoder) cds.comp69611_c0_seq1|m.21415(Tcoc_longest.fasta.transdecoder) cds.comp137969_c0_seq1|m.38834(Tcoc_longest.fasta.transdecoder) cds.comp50446_c0_seq1|m.10812(Tcoc_longest.fasta.transdecoder) cds.comp118247_c0_seq1|m.37034(Tcoc_longest.fasta.transdecoder) cds.comp22878_c0_seq1|m.3754(Tcoc_longest.fasta.transdecoder) cds.comp55243_c0_seq1|m.12869(Tcoc_longest.fasta.transdecoder) cds.comp39065_c0_seq2|m.7346(Tcoc_longest.fasta.transdecoder) cds.comp70546_c0_seq1|m.22173(Tcoc_longest.fasta.transdecoder) cds.comp71270_c0_seq1|m.22748(Tcoc_longest.fasta.transdecoder) cds.comp74144_c0_seq1|m.25371(Tcoc_longest.fasta.transdecoder) cds.comp56350_c0_seq1|m.13429(Tcoc_longest.fasta.transdecoder) cds.comp51708_c0_seq1|m.11307(Tcoc_longest.fasta.transdecoder) cds.comp66037_c0_seq1|m.18866(Tcoc_longest.fasta.transdecoder) cds.comp59759_c0_seq1|m.15185(Tcoc_longest.fasta.transdecoder) cds.comp60208_c0_seq1|m.15399(Tcoc_longest.fasta.transdecoder) cds.comp66092_c0_seq1|m.18902(Tcoc_longest.fasta.transdecoder) cds.comp35402_c0_seq1|m.6495(Tcoc_longest.fasta.transdecoder) cds.comp27133_c0_seq2|m.4610(Tcoc_longest.fasta.transdecoder) cds.comp41092_c0_seq1|m.7871(Tmic_longest.fasta.transdecoder)
ORTHOMCL4 (22 genes,3 taxa):     cds.comp4857_c0_seq9|m.1481(Peve_longest.fasta.transdecoder) cds.comp15005_c0_seq1|m.4778(Plob_longest.fasta.transdecoder) cds.comp60320_c0_seq2|m.15453(Tcoc_longest.fasta.transdecoder) cds.comp93671_c0_seq1|m.33222(Tcoc_longest.fasta.transdecoder) cds.comp104382_c0_seq1|m.35120(Tcoc_longest.fasta.transdecoder) cds.comp42213_c0_seq1|m.8107(Tcoc_longest.fasta.transdecoder) cds.comp76544_c0_seq3|m.27930(Tcoc_longest.fasta.transdecoder) cds.comp77777_c0_seq20|m.29345(Tcoc_longest.fasta.transdecoder) cds.comp68315_c0_seq1|m.20420(Tcoc_longest.fasta.transdecoder) cds.comp66712_c0_seq1|m.19303(Tcoc_longest.fasta.transdecoder) cds.comp48341_c0_seq2|m.10136(Tcoc_longest.fasta.transdecoder) cds.comp77098_c0_seq1|m.28573(Tcoc_longest.fasta.transdecoder) cds.comp62536_c0_seq1|m.16673(Tcoc_longest.fasta.transdecoder) cds.comp71803_c0_seq1|m.23195(Tcoc_longest.fasta.transdecoder) cds.comp90237_c0_seq1|m.32507(Tcoc_longest.fasta.transdecoder) cds.comp74890_c0_seq1|m.26122(Tcoc_longest.fasta.transdecoder) cds.comp122357_c0_seq1|m.37469(Tcoc_longest.fasta.transdecoder) cds.comp31002_c0_seq1|m.5546(Tcoc_longest.fasta.transdecoder) cds.comp25843_c0_seq2|m.4316(Tcoc_longest.fasta.transdecoder) cds.comp23822_c0_seq1|m.3957(Tcoc_longest.fasta.transdecoder) cds.comp12981_c0_seq1|m.1460(Tcoc_longest.fasta.transdecoder) cds.comp27322_c0_seq2|m.4654(Tcoc_longest.fasta.transdecoder)
ORTHOMCL5 (21 genes,5 taxa):     cds.comp3190_c0_seq1|m.471(Daxi_longest.fasta.transdecoder) cds.comp2915_c0_seq1|m.752(Peve_longest.fasta.transdecoder) cds.comp4975_c0_seq1|m.1539(Peve_longest.fasta.transdecoder) cds.comp11594_c0_seq1|m.3261(Plob_longest.fasta.transdecoder) cds.comp12135_c0_seq4|m.3464(Plob_longest.fasta.transdecoder) cds.comp97719_c0_seq1|m.33986(Tcoc_longest.fasta.transdecoder) cds.comp74414_c0_seq2|m.25657(Tcoc_longest.fasta.transdecoder) cds.comp77546_c0_seq1|m.29085(Tcoc_longest.fasta.transdecoder) cds.comp77127_c2_seq1|m.28613(Tcoc_longest.fasta.transdecoder) cds.comp76330_c0_seq13|m.27681(Tcoc_longest.fasta.transdecoder) cds.comp74716_c0_seq1|m.25961(Tcoc_longest.fasta.transdecoder) cds.comp74577_c0_seq1|m.25818(Tcoc_longest.fasta.transdecoder) cds.comp75933_c0_seq1|m.27261(Tcoc_longest.fasta.transdecoder) cds.comp74154_c0_seq2|m.25380(Tcoc_longest.fasta.transdecoder) cds.comp70521_c0_seq3|m.22156(Tcoc_longest.fasta.transdecoder) cds.comp55289_c0_seq1|m.12895(Tcoc_longest.fasta.transdecoder) cds.comp35987_c0_seq1|m.7435(Tmic_longest.fasta.transdecoder) cds.comp15476_c0_seq1|m.4195(Tmic_longest.fasta.transdecoder) cds.comp16861_c0_seq1|m.4808(Tmic_longest.fasta.transdecoder) cds.comp3514_c0_seq1|m.537(Tmic_longest.fasta.transdecoder) cds.comp27815_c0_seq1|m.6605(Tmic_longest.fasta.transdecoder)
ORTHOMCL6 (21 genes,5 taxa):     cds.comp7280_c0_seq1|m.1368(Pcom_longest.fasta.transdecoder) cds.comp5655_c0_seq1|m.1142(Pcom_longest.fasta.transdecoder) cds.comp9444_c0_seq1|m.2974(Peve_longest.fasta.transdecoder) cds.comp2950_c0_seq1|m.765(Peve_longest.fasta.transdecoder) cds.comp5915_c0_seq1|m.2028(Peve_longest.fasta.transdecoder) cds.comp8490_c0_seq1|m.2742(Peve_longest.fasta.transdecoder) cds.comp9704_c0_seq3|m.2584(Plob_longest.fasta.transdecoder) cds.comp29265_c0_seq1|m.7887(Plob_longest.fasta.transdecoder) cds.comp31113_c0_seq1|m.8076(Plob_longest.fasta.transdecoder) cds.comp17070_c0_seq1|m.5565(Plob_longest.fasta.transdecoder) cds.comp100376_c0_seq1|m.34457(Tcoc_longest.fasta.transdecoder) cds.comp58949_c0_seq1|m.14792(Tcoc_longest.fasta.transdecoder) cds.comp66860_c0_seq1|m.19408(Tcoc_longest.fasta.transdecoder) cds.comp72030_c0_seq1|m.23402(Tcoc_longest.fasta.transdecoder) cds.comp76900_c0_seq1|m.28328(Tcoc_longest.fasta.transdecoder) cds.comp75026_c0_seq2|m.26260(Tcoc_longest.fasta.transdecoder) cds.comp77219_c0_seq5|m.28708(Tcoc_longest.fasta.transdecoder) cds.comp75603_c0_seq1|m.26879(Tcoc_longest.fasta.transdecoder) cds.comp67558_c0_seq1|m.19906(Tcoc_longest.fasta.transdecoder) cds.comp63462_c0_seq2|m.17205(Tcoc_longest.fasta.transdecoder) cds.comp7471_c0_seq1|m.1373(Tmic_longest.fasta.transdecoder)
ORTHOMCL7 (21 genes,1 taxa):     cds.comp78646_c0_seq1|m.29719(Tcoc_longest.fasta.transdecoder) cds.comp64362_c0_seq1|m.17795(Tcoc_longest.fasta.transdecoder) cds.comp109501_c0_seq1|m.35873(Tcoc_longest.fasta.transdecoder) cds.comp113274_c0_seq1|m.36365(Tcoc_longest.fasta.transdecoder) cds.comp77483_c1_seq2|m.29005(Tcoc_longest.fasta.transdecoder) cds.comp75135_c1_seq1|m.26374(Tcoc_longest.fasta.transdecoder) cds.comp71136_c0_seq1|m.22646(Tcoc_longest.fasta.transdecoder) cds.comp77574_c0_seq2|m.29108(Tcoc_longest.fasta.transdecoder) cds.comp73948_c0_seq3|m.25160(Tcoc_longest.fasta.transdecoder) cds.comp32434_c0_seq2|m.5870(Tcoc_longest.fasta.transdecoder) cds.comp87140_c0_seq1|m.31807(Tcoc_longest.fasta.transdecoder) cds.comp50613_c0_seq4|m.10879(Tcoc_longest.fasta.transdecoder) cds.comp59838_c0_seq1|m.15218(Tcoc_longest.fasta.transdecoder) cds.comp50479_c0_seq1|m.10822(Tcoc_longest.fasta.transdecoder) cds.comp67627_c0_seq2|m.19952(Tcoc_longest.fasta.transdecoder) cds.comp34144_c0_seq1|m.6241(Tcoc_longest.fasta.transdecoder) cds.comp24283_c0_seq1|m.4036(Tcoc_longest.fasta.transdecoder) cds.comp14439_c0_seq1|m.1817(Tcoc_longest.fasta.transdecoder) cds.comp116786_c0_seq1|m.36850(Tcoc_longest.fasta.transdecoder) cds.comp23485_c0_seq1|m.3893(Tcoc_longest.fasta.transdecoder) cds.comp24334_c0_seq1|m.4044(Tcoc_longest.fasta.transdecoder)
ORTHOMCL8 (20 genes,6 taxa):     cds.comp8581_c0_seq1|m.1361(Daxi_longest.fasta.transdecoder) cds.comp10586_c0_seq3|m.1918(Daxi_longest.fasta.transdecoder) cds.comp5767_c0_seq1|m.863(Daxi_longest.fasta.transdecoder) cds.comp4681_c0_seq1|m.1022(Pcom_longest.fasta.transdecoder) cds.comp7655_c0_seq1|m.1416(Pcom_longest.fasta.transdecoder) cds.comp12620_c0_seq1|m.1871(Pcom_longest.fasta.transdecoder) cds.comp3847_c0_seq1|m.1056(Peve_longest.fasta.transdecoder) cds.comp5199_c0_seq1|m.1661(Peve_longest.fasta.transdecoder) cds.comp3702_c0_seq1|m.1007(Peve_longest.fasta.transdecoder) cds.comp13855_c0_seq1|m.4240(Plob_longest.fasta.transdecoder) cds.comp5847_c0_seq1|m.1469(Plob_longest.fasta.transdecoder) cds.comp41400_c0_seq1|m.8862(Plob_longest.fasta.transdecoder) cds.comp271_c0_seq1|m.30(Plob_longest.fasta.transdecoder) cds.comp19597_c0_seq1|m.6236(Plob_longest.fasta.transdecoder) cds.comp28817_c0_seq1|m.5019(Tcoc_longest.fasta.transdecoder) cds.comp77776_c0_seq4|m.29339(Tcoc_longest.fasta.transdecoder) cds.comp8591_c0_seq1|m.1789(Tmic_longest.fasta.transdecoder) cds.comp3048_c0_seq1|m.437(Tmic_longest.fasta.transdecoder) cds.comp33595_c0_seq1|m.7190(Tmic_longest.fasta.transdecoder) cds.comp2766_c0_seq1|m.374(Tmic_longest.fasta.transdecoder)
ORTHOMCL9 (19 genes,2 taxa):     cds.comp2836_c0_seq1|m.709(Peve_longest.fasta.transdecoder) cds.comp140656_c0_seq1|m.39060(Tcoc_longest.fasta.transdecoder) cds.comp109016_c0_seq1|m.35795(Tcoc_longest.fasta.transdecoder) cds.comp80685_c0_seq1|m.30286(Tcoc_longest.fasta.transdecoder) cds.comp50044_c0_seq1|m.10684(Tcoc_longest.fasta.transdecoder) cds.comp91965_c0_seq1|m.32878(Tcoc_longest.fasta.transdecoder) cds.comp119449_c0_seq1|m.37152(Tcoc_longest.fasta.transdecoder) cds.comp67709_c0_seq1|m.20008(Tcoc_longest.fasta.transdecoder) cds.comp74162_c0_seq2|m.25388(Tcoc_longest.fasta.transdecoder) cds.comp78641_c0_seq1|m.29717(Tcoc_longest.fasta.transdecoder) cds.comp16397_c0_seq1|m.2393(Tcoc_longest.fasta.transdecoder) cds.comp32086_c0_seq1|m.5793(Tcoc_longest.fasta.transdecoder) cds.comp83666_c0_seq1|m.30984(Tcoc_longest.fasta.transdecoder) cds.comp83954_c0_seq1|m.31053(Tcoc_longest.fasta.transdecoder) cds.comp121003_c0_seq1|m.37296(Tcoc_longest.fasta.transdecoder) cds.comp28636_c0_seq1|m.4977(Tcoc_longest.fasta.transdecoder) cds.comp158366_c0_seq1|m.40047(Tcoc_longest.fasta.transdecoder) cds.comp59627_c0_seq1|m.15124(Tcoc_longest.fasta.transdecoder) cds.comp43837_c0_seq1|m.8636(Tcoc_longest.fasta.transdecoder)
```

Output: Each ortholog contains at least 2 species from each of 2 clades
```
ORTHOMCL5 (21 genes,5 taxa):     cds.comp3190_c0_seq1|m.471(Daxi_longest.fasta.transdecoder) cds.comp2915_c0_seq1|m.752(Peve_longest.fasta.transdecoder) cds.comp4975_c0_seq1|m.1539(Peve_longest.fasta.transdecoder) cds.comp11594_c0_seq1|m.3261(Plob_longest.fasta.transdecoder) cds.comp12135_c0_seq4|m.3464(Plob_longest.fasta.transdecoder) cds.comp97719_c0_seq1|m.33986(Tcoc_longest.fasta.transdecoder) cds.comp74414_c0_seq2|m.25657(Tcoc_longest.fasta.transdecoder) cds.comp77546_c0_seq1|m.29085(Tcoc_longest.fasta.transdecoder) cds.comp77127_c2_seq1|m.28613(Tcoc_longest.fasta.transdecoder) cds.comp76330_c0_seq13|m.27681(Tcoc_longest.fasta.transdecoder) cds.comp74716_c0_seq1|m.25961(Tcoc_longest.fasta.transdecoder) cds.comp74577_c0_seq1|m.25818(Tcoc_longest.fasta.transdecoder) cds.comp75933_c0_seq1|m.27261(Tcoc_longest.fasta.transdecoder) cds.comp74154_c0_seq2|m.25380(Tcoc_longest.fasta.transdecoder) cds.comp70521_c0_seq3|m.22156(Tcoc_longest.fasta.transdecoder) cds.comp55289_c0_seq1|m.12895(Tcoc_longest.fasta.transdecoder) cds.comp35987_c0_seq1|m.7435(Tmic_longest.fasta.transdecoder) cds.comp15476_c0_seq1|m.4195(Tmic_longest.fasta.transdecoder) cds.comp16861_c0_seq1|m.4808(Tmic_longest.fasta.transdecoder) cds.comp3514_c0_seq1|m.537(Tmic_longest.fasta.transdecoder) cds.comp27815_c0_seq1|m.6605(Tmic_longest.fasta.transdecoder)
ORTHOMCL6 (21 genes,5 taxa):     cds.comp7280_c0_seq1|m.1368(Pcom_longest.fasta.transdecoder) cds.comp5655_c0_seq1|m.1142(Pcom_longest.fasta.transdecoder) cds.comp9444_c0_seq1|m.2974(Peve_longest.fasta.transdecoder) cds.comp2950_c0_seq1|m.765(Peve_longest.fasta.transdecoder) cds.comp5915_c0_seq1|m.2028(Peve_longest.fasta.transdecoder) cds.comp8490_c0_seq1|m.2742(Peve_longest.fasta.transdecoder) cds.comp9704_c0_seq3|m.2584(Plob_longest.fasta.transdecoder) cds.comp29265_c0_seq1|m.7887(Plob_longest.fasta.transdecoder) cds.comp31113_c0_seq1|m.8076(Plob_longest.fasta.transdecoder) cds.comp17070_c0_seq1|m.5565(Plob_longest.fasta.transdecoder) cds.comp100376_c0_seq1|m.34457(Tcoc_longest.fasta.transdecoder) cds.comp58949_c0_seq1|m.14792(Tcoc_longest.fasta.transdecoder) cds.comp66860_c0_seq1|m.19408(Tcoc_longest.fasta.transdecoder) cds.comp72030_c0_seq1|m.23402(Tcoc_longest.fasta.transdecoder) cds.comp76900_c0_seq1|m.28328(Tcoc_longest.fasta.transdecoder) cds.comp75026_c0_seq2|m.26260(Tcoc_longest.fasta.transdecoder) cds.comp77219_c0_seq5|m.28708(Tcoc_longest.fasta.transdecoder) cds.comp75603_c0_seq1|m.26879(Tcoc_longest.fasta.transdecoder) cds.comp67558_c0_seq1|m.19906(Tcoc_longest.fasta.transdecoder) cds.comp63462_c0_seq2|m.17205(Tcoc_longest.fasta.transdecoder) cds.comp7471_c0_seq1|m.1373(Tmic_longest.fasta.transdecoder)
ORTHOMCL8 (20 genes,6 taxa):     cds.comp8581_c0_seq1|m.1361(Daxi_longest.fasta.transdecoder) cds.comp10586_c0_seq3|m.1918(Daxi_longest.fasta.transdecoder) cds.comp5767_c0_seq1|m.863(Daxi_longest.fasta.transdecoder) cds.comp4681_c0_seq1|m.1022(Pcom_longest.fasta.transdecoder) cds.comp7655_c0_seq1|m.1416(Pcom_longest.fasta.transdecoder) cds.comp12620_c0_seq1|m.1871(Pcom_longest.fasta.transdecoder) cds.comp3847_c0_seq1|m.1056(Peve_longest.fasta.transdecoder) cds.comp5199_c0_seq1|m.1661(Peve_longest.fasta.transdecoder) cds.comp3702_c0_seq1|m.1007(Peve_longest.fasta.transdecoder) cds.comp13855_c0_seq1|m.4240(Plob_longest.fasta.transdecoder) cds.comp5847_c0_seq1|m.1469(Plob_longest.fasta.transdecoder) cds.comp41400_c0_seq1|m.8862(Plob_longest.fasta.transdecoder) cds.comp271_c0_seq1|m.30(Plob_longest.fasta.transdecoder) cds.comp19597_c0_seq1|m.6236(Plob_longest.fasta.transdecoder) cds.comp28817_c0_seq1|m.5019(Tcoc_longest.fasta.transdecoder) cds.comp77776_c0_seq4|m.29339(Tcoc_longest.fasta.transdecoder) cds.comp8591_c0_seq1|m.1789(Tmic_longest.fasta.transdecoder) cds.comp3048_c0_seq1|m.437(Tmic_longest.fasta.transdecoder) cds.comp33595_c0_seq1|m.7190(Tmic_longest.fasta.transdecoder) cds.comp2766_c0_seq1|m.374(Tmic_longest.fasta.transdecoder)
```
