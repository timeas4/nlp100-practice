#アナロジーデータでの実験
from gensim.models import KeyedVectors

# 学習済みword2vecモデルを読み込む（.binなのでbinary=True）
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

# 評価データを読み込み、各事例にアナロジーを適用する
# 出力ファイルに「セクション名 / 元の4単語 / 予測単語 / 類似度」を記録する
with open('questions-words.txt', 'r', encoding='utf-8') as f_in, \
     open('questions-words-result.txt', 'w', encoding='utf-8') as f_out:

    section = ''  # 現在のセクション名を保持する

    for line in f_in:
        line = line.strip()

        # ": セクション名" の行ならセクションを更新して次へ
        if line.startswith(':'):
            section = line[2:]  # ": " を除いた部分
            continue

        # 4単語に分割（1列目 2列目 3列目 4列目=正解）
        words = line.split()

        # vec(2列目) - vec(1列目) + vec(3列目) に最も近い1語を求める
        # positive=[2列目, 3列目], negative=[1列目]
        predicted, similarity = model.most_similar(
            positive=[words[1], words[2]],
            negative=[words[0]],
            topn=1
        )[0]

        # セクション名・元の4単語・予測単語・類似度を1行に記録する
        f_out.write(f'{section} {line} {predicted} {similarity}\n')

'''
前300件の結果
apital-common-countries Athens Greece Baghdad Iraq Iraqi 0.6351872086524963
capital-common-countries Athens Greece Bangkok Thailand Thailand 0.7137668132781982
capital-common-countries Athens Greece Beijing China China 0.7235777378082275
capital-common-countries Athens Greece Berlin Germany Germany 0.6734622716903687
capital-common-countries Athens Greece Bern Switzerland Switzerland 0.49197492003440857
capital-common-countries Athens Greece Cairo Egypt Egypt 0.7527809739112854
capital-common-countries Athens Greece Canberra Australia Australia 0.583732545375824
capital-common-countries Athens Greece Hanoi Vietnam Viet_Nam 0.6276341676712036
capital-common-countries Athens Greece Havana Cuba Cuba 0.6460992693901062
capital-common-countries Athens Greece Helsinki Finland Finland 0.6899983286857605
capital-common-countries Athens Greece Islamabad Pakistan Pakistan 0.7233326435089111
capital-common-countries Athens Greece Kabul Afghanistan Afghan 0.6160915493965149
capital-common-countries Athens Greece London England Britain 0.5646187663078308
capital-common-countries Athens Greece Madrid Spain Spain 0.7036612629890442
capital-common-countries Athens Greece Moscow Russia Russia 0.7382973432540894
capital-common-countries Athens Greece Oslo Norway Norway 0.6470744013786316
capital-common-countries Athens Greece Ottawa Canada Canada 0.5912168025970459
capital-common-countries Athens Greece Paris France France 0.6724624037742615
capital-common-countries Athens Greece Rome Italy Italy 0.6826189756393433
capital-common-countries Athens Greece Stockholm Sweden Sweden 0.6757243871688843
capital-common-countries Athens Greece Tehran Iran Iran 0.7671369314193726
capital-common-countries Athens Greece Tokyo Japan Japan 0.7256094813346863
capital-common-countries Baghdad Iraq Bangkok Thailand Thailand 0.6745355129241943
capital-common-countries Baghdad Iraq Beijing China China 0.6915649175643921
capital-common-countries Baghdad Iraq Berlin Germany Germany 0.6057409048080444
capital-common-countries Baghdad Iraq Bern Switzerland coach_Bobby_Curlings 0.4347156882286072
capital-common-countries Baghdad Iraq Cairo Egypt Egypt 0.6848487257957458
capital-common-countries Baghdad Iraq Canberra Australia Mr_Rudd 0.6186109185218811
capital-common-countries Baghdad Iraq Hanoi Vietnam Vietnam 0.7493551969528198
capital-common-countries Baghdad Iraq Havana Cuba Cuba 0.7133255004882812
capital-common-countries Baghdad Iraq Helsinki Finland Finland 0.5972561836242676
capital-common-countries Baghdad Iraq Islamabad Pakistan Pakistan 0.7466936707496643
capital-common-countries Baghdad Iraq Kabul Afghanistan Afghanistan 0.8359360098838806
capital-common-countries Baghdad Iraq London England Britain 0.5853632092475891
capital-common-countries Baghdad Iraq Madrid Spain Spain 0.6144677400588989
capital-common-countries Baghdad Iraq Moscow Russia Russia 0.7236210107803345
capital-common-countries Baghdad Iraq Oslo Norway Norway 0.5987579822540283
capital-common-countries Baghdad Iraq Ottawa Canada Prime_Minister_Jean_Chrétien 0.5704855918884277
capital-common-countries Baghdad Iraq Paris France France 0.6203721165657043
capital-common-countries Baghdad Iraq Rome Italy Italy 0.5362658500671387
capital-common-countries Baghdad Iraq Stockholm Sweden Sweden 0.5907803177833557
capital-common-countries Baghdad Iraq Tehran Iran Iran 0.8114986419677734
capital-common-countries Baghdad Iraq Tokyo Japan Japan 0.7056295871734619
capital-common-countries Baghdad Iraq Athens Greece Greece 0.5793530344963074
capital-common-countries Bangkok Thailand Beijing China China 0.8263983726501465
capital-common-countries Bangkok Thailand Berlin Germany Germany 0.7295198440551758
capital-common-countries Bangkok Thailand Bern Switzerland Switzerland 0.5047770142555237
capital-common-countries Bangkok Thailand Cairo Egypt Egypt 0.8118714690208435
capital-common-countries Bangkok Thailand Canberra Australia Australia 0.7154911160469055
capital-common-countries Bangkok Thailand Hanoi Vietnam Viet_Nam 0.7700589895248413
capital-common-countries Bangkok Thailand Havana Cuba Cuba 0.800740659236908
capital-common-countries Bangkok Thailand Helsinki Finland Finland 0.7515272498130798
capital-common-countries Bangkok Thailand Islamabad Pakistan Pakistan 0.797675371170044
capital-common-countries Bangkok Thailand Kabul Afghanistan Afghanistan 0.6666890382766724
capital-common-countries Bangkok Thailand London England Britain 0.6576253771781921
capital-common-countries Bangkok Thailand Madrid Spain Spain 0.765529990196228
capital-common-countries Bangkok Thailand Moscow Russia Russia 0.8613657355308533
capital-common-countries Bangkok Thailand Oslo Norway Norway 0.7142738103866577
capital-common-countries Bangkok Thailand Ottawa Canada Canada 0.6684818267822266
capital-common-countries Bangkok Thailand Paris France France 0.7388159036636353
capital-common-countries Bangkok Thailand Rome Italy Italy 0.6863130331039429
capital-common-countries Bangkok Thailand Stockholm Sweden Sweden 0.7587180733680725
capital-common-countries Bangkok Thailand Tehran Iran Iran 0.8363438248634338
capital-common-countries Bangkok Thailand Tokyo Japan Japan 0.8282636404037476
capital-common-countries Bangkok Thailand Athens Greece Greece 0.6765021681785583
capital-common-countries Bangkok Thailand Baghdad Iraq Iraqi 0.6885136365890503
capital-common-countries Beijing China Berlin Germany Germany 0.7232257723808289
capital-common-countries Beijing China Bern Switzerland Bern_NC 0.4655816853046417
capital-common-countries Beijing China Cairo Egypt Egypt 0.7653077244758606
capital-common-countries Beijing China Canberra Australia Australia 0.7234395146369934
capital-common-countries Beijing China Hanoi Vietnam Viet_Nam 0.7793147563934326
capital-common-countries Beijing China Havana Cuba Cuba 0.7189656496047974
capital-common-countries Beijing China Helsinki Finland Finland 0.7141392230987549
capital-common-countries Beijing China Islamabad Pakistan Pakistan 0.8062406182289124
capital-common-countries Beijing China Kabul Afghanistan Afghan 0.6770889163017273
capital-common-countries Beijing China London England UK 0.6304796934127808
capital-common-countries Beijing China Madrid Spain Spain 0.7320305109024048
capital-common-countries Beijing China Moscow Russia Russia 0.8579800128936768
capital-common-countries Beijing China Oslo Norway Norway 0.6628976464271545
capital-common-countries Beijing China Ottawa Canada Canada 0.6537172794342041
capital-common-countries Beijing China Paris France France 0.7109121680259705
capital-common-countries Beijing China Rome Italy Italy 0.663748562335968
capital-common-countries Beijing China Stockholm Sweden Sweden 0.7026647925376892
capital-common-countries Beijing China Tehran Iran Iran 0.8262744545936584
capital-common-countries Beijing China Tokyo Japan Japan 0.8236700892448425
capital-common-countries Beijing China Athens Greece Greece 0.6515148878097534
capital-common-countries Beijing China Baghdad Iraq Mosul 0.7041886448860168
capital-common-countries Beijing China Bangkok Thailand Thailand 0.8047244548797607
capital-common-countries Berlin Germany Bern Switzerland Switzerland 0.609531819820404
capital-common-countries Berlin Germany Cairo Egypt Egypt 0.691230833530426
capital-common-countries Berlin Germany Canberra Australia Australia 0.7485095858573914
capital-common-countries Berlin Germany Hanoi Vietnam Viet_Nam 0.6875089406967163
capital-common-countries Berlin Germany Havana Cuba Cuba 0.6961180567741394
capital-common-countries Berlin Germany Helsinki Finland Finland 0.7654494643211365
capital-common-countries Berlin Germany Islamabad Pakistan Pakistan 0.7597626447677612
capital-common-countries Berlin Germany Kabul Afghanistan Afghan 0.6450541019439697
capital-common-countries Berlin Germany London England UK 0.6597434878349304
capital-common-countries Berlin Germany Madrid Spain Spain 0.7768210172653198
capital-common-countries Berlin Germany Moscow Russia Russia 0.8107380867004395
capital-common-countries Berlin Germany Oslo Norway Norway 0.7291736006736755
capital-common-countries Berlin Germany Ottawa Canada Canada 0.6773227453231812
capital-common-countries Berlin Germany Paris France France 0.7884092926979065
capital-common-countries Berlin Germany Rome Italy Italy 0.7509608268737793
capital-common-countries Berlin Germany Stockholm Sweden Sweden 0.8022658228874207
capital-common-countries Berlin Germany Tehran Iran Iran 0.7747756838798523
capital-common-countries Berlin Germany Tokyo Japan Japan 0.7969788312911987
capital-common-countries Berlin Germany Athens Greece Greece 0.6390470862388611
capital-common-countries Berlin Germany Baghdad Iraq Mosul 0.686406135559082
capital-common-countries Berlin Germany Bangkok Thailand Thailand 0.768083393573761
capital-common-countries Berlin Germany Beijing China China 0.7755853533744812
capital-common-countries Bern Switzerland Cairo Egypt Egypt 0.5989274382591248
capital-common-countries Bern Switzerland Canberra Australia Australia 0.6860507130622864
capital-common-countries Bern Switzerland Hanoi Vietnam Viet_Nam 0.5609371066093445
capital-common-countries Bern Switzerland Havana Cuba Cuba 0.6295958757400513
capital-common-countries Bern Switzerland Helsinki Finland Finland 0.6637657880783081
capital-common-countries Bern Switzerland Islamabad Pakistan Pakistan 0.6708023548126221
capital-common-countries Bern Switzerland Kabul Afghanistan Afghanistan 0.5338184833526611
capital-common-countries Bern Switzerland London England EURASIAN_NATURAL_RESOURCES_CORP. 0.5463826060295105
capital-common-countries Bern Switzerland Madrid Spain Spain 0.6423718333244324
capital-common-countries Bern Switzerland Moscow Russia Russia 0.6487588882446289
capital-common-countries Bern Switzerland Oslo Norway Norway 0.6448377966880798
capital-common-countries Bern Switzerland Ottawa Canada Canada 0.646811306476593
capital-common-countries Bern Switzerland Paris France France 0.6129553318023682
capital-common-countries Bern Switzerland Rome Italy Italy 0.6486327052116394
capital-common-countries Bern Switzerland Stockholm Sweden Sweden 0.684966504573822
capital-common-countries Bern Switzerland Tehran Iran Iran 0.6813835501670837
capital-common-countries Bern Switzerland Tokyo Japan Japan 0.6434275507926941
capital-common-countries Bern Switzerland Athens Greece Greece 0.580009937286377
capital-common-countries Bern Switzerland Baghdad Iraq Iraqi 0.5730240941047668
capital-common-countries Bern Switzerland Bangkok Thailand Thailand 0.661731481552124
capital-common-countries Bern Switzerland Beijing China China 0.6225298047065735
capital-common-countries Bern Switzerland Berlin Germany Germany 0.7138351202011108
capital-common-countries Cairo Egypt Canberra Australia Australia 0.6811554431915283
capital-common-countries Cairo Egypt Hanoi Vietnam Viet_Nam 0.7589392066001892
capital-common-countries Cairo Egypt Havana Cuba Cuba 0.7639016509056091
capital-common-countries Cairo Egypt Helsinki Finland Finland 0.7256742715835571
capital-common-countries Cairo Egypt Islamabad Pakistan Pakistan 0.8155919313430786
capital-common-countries Cairo Egypt Kabul Afghanistan Afghan 0.6829641461372375
capital-common-countries Cairo Egypt London England Britain 0.6454266905784607
capital-common-countries Cairo Egypt Madrid Spain Spain 0.7469132542610168
capital-common-countries Cairo Egypt Moscow Russia Russia 0.8426570892333984
capital-common-countries Cairo Egypt Oslo Norway Norway 0.6975642442703247
capital-common-countries Cairo Egypt Ottawa Canada Canada 0.6659149527549744
capital-common-countries Cairo Egypt Paris France France 0.7114198207855225
capital-common-countries Cairo Egypt Rome Italy Italy 0.6812829971313477
capital-common-countries Cairo Egypt Stockholm Sweden Sweden 0.7365163564682007
capital-common-countries Cairo Egypt Tehran Iran Iran 0.8531845211982727
capital-common-countries Cairo Egypt Tokyo Japan Japan 0.775351881980896
capital-common-countries Cairo Egypt Athens Greece Greece 0.7355355620384216
capital-common-countries Cairo Egypt Baghdad Iraq Iraqi 0.7208045721054077
capital-common-countries Cairo Egypt Bangkok Thailand Thailand 0.8275741934776306
capital-common-countries Cairo Egypt Beijing China China 0.8066043257713318
capital-common-countries Cairo Egypt Berlin Germany Germany 0.7016904950141907
capital-common-countries Cairo Egypt Bern Switzerland Switzerland 0.4930407404899597
capital-common-countries Canberra Australia Hanoi Vietnam Viet_Nam 0.6714491248130798
capital-common-countries Canberra Australia Havana Cuba Cuba 0.6964417695999146
capital-common-countries Canberra Australia Helsinki Finland Finland 0.690654993057251
capital-common-countries Canberra Australia Islamabad Pakistan Pakistan 0.7743954658508301
capital-common-countries Canberra Australia Kabul Afghanistan Afghans 0.5854719281196594
capital-common-countries Canberra Australia London England UK 0.6224532723426819
capital-common-countries Canberra Australia Madrid Spain Spain 0.7410276532173157
capital-common-countries Canberra Australia Moscow Russia Russia 0.7891086339950562
capital-common-countries Canberra Australia Oslo Norway Norway 0.6703748106956482
capital-common-countries Canberra Australia Ottawa Canada Canada 0.7492119669914246
capital-common-countries Canberra Australia Paris France France 0.7159996032714844
capital-common-countries Canberra Australia Rome Italy Italy 0.663947343826294
capital-common-countries Canberra Australia Stockholm Sweden Sweden 0.706972062587738
capital-common-countries Canberra Australia Tehran Iran Iran 0.7551094889640808
capital-common-countries Canberra Australia Tokyo Japan Japan 0.7584798336029053
capital-common-countries Canberra Australia Athens Greece Greece 0.5700703263282776
capital-common-countries Canberra Australia Baghdad Iraq Mosul 0.6397027969360352
capital-common-countries Canberra Australia Bangkok Thailand Thailand 0.7358657121658325
capital-common-countries Canberra Australia Beijing China China 0.7823367714881897
capital-common-countries Canberra Australia Berlin Germany Germany 0.7441056370735168
capital-common-countries Canberra Australia Bern Switzerland Switzerland 0.5360246300697327
capital-common-countries Canberra Australia Cairo Egypt Egypt 0.6859406232833862
capital-common-countries Hanoi Vietnam Havana Cuba Cuba 0.6831809878349304
capital-common-countries Hanoi Vietnam Helsinki Finland Finland 0.5732652544975281
capital-common-countries Hanoi Vietnam Islamabad Pakistan Pakistan 0.7073384523391724
capital-common-countries Hanoi Vietnam Kabul Afghanistan Afghanistan 0.7566174864768982
capital-common-countries Hanoi Vietnam London England Britain 0.532074511051178
capital-common-countries Hanoi Vietnam Madrid Spain Spain 0.6318690776824951
capital-common-countries Hanoi Vietnam Moscow Russia Russia 0.6925882697105408
capital-common-countries Hanoi Vietnam Oslo Norway Norway 0.5300316214561462
capital-common-countries Hanoi Vietnam Ottawa Canada Canada 0.5802633762359619
capital-common-countries Hanoi Vietnam Paris France France 0.5821924209594727
capital-common-countries Hanoi Vietnam Rome Italy Italy 0.5208398699760437
capital-common-countries Hanoi Vietnam Stockholm Sweden Sweden 0.5909290313720703
capital-common-countries Hanoi Vietnam Tehran Iran Iran 0.7381365895271301
capital-common-countries Hanoi Vietnam Tokyo Japan Japan 0.6836792826652527
capital-common-countries Hanoi Vietnam Athens Greece Greece 0.5295499563217163
capital-common-countries Hanoi Vietnam Baghdad Iraq Iraq 0.7784610986709595
capital-common-countries Hanoi Vietnam Bangkok Thailand Thailand 0.6948618292808533
capital-common-countries Hanoi Vietnam Beijing China China 0.7234393358230591
capital-common-countries Hanoi Vietnam Berlin Germany Germany 0.5970561504364014
capital-common-countries Hanoi Vietnam Bern Switzerland Bern_NC 0.4975764751434326
capital-common-countries Hanoi Vietnam Cairo Egypt Egypt 0.70243239402771
capital-common-countries Hanoi Vietnam Canberra Australia Australia 0.6169843673706055
capital-common-countries Havana Cuba Helsinki Finland Finland 0.6971814036369324
capital-common-countries Havana Cuba Islamabad Pakistan Pakistan 0.8123713731765747
capital-common-countries Havana Cuba Kabul Afghanistan Afghanistan 0.7092918157577515
capital-common-countries Havana Cuba London England Britain 0.6217108368873596
capital-common-countries Havana Cuba Madrid Spain Spain 0.6929836869239807
capital-common-countries Havana Cuba Moscow Russia Russia 0.8237831592559814
capital-common-countries Havana Cuba Oslo Norway Norway 0.7030717134475708
capital-common-countries Havana Cuba Ottawa Canada Canada 0.6562577486038208
capital-common-countries Havana Cuba Paris France France 0.6843083500862122
capital-common-countries Havana Cuba Rome Italy Italy 0.6025851964950562
capital-common-countries Havana Cuba Stockholm Sweden Sweden 0.7303111553192139
capital-common-countries Havana Cuba Tehran Iran Iran 0.8635510206222534
capital-common-countries Havana Cuba Tokyo Japan Japan 0.7725997567176819
capital-common-countries Havana Cuba Athens Greece Greece 0.632399320602417
capital-common-countries Havana Cuba Baghdad Iraq Iraq 0.7371042966842651
capital-common-countries Havana Cuba Bangkok Thailand Thailand 0.7950247526168823
capital-common-countries Havana Cuba Beijing China China 0.7704690098762512
capital-common-countries Havana Cuba Berlin Germany Germany 0.6952270269393921
capital-common-countries Havana Cuba Bern Switzerland Switzerland 0.502707302570343
capital-common-countries Havana Cuba Cairo Egypt Egypt 0.7647275924682617
capital-common-countries Havana Cuba Canberra Australia Australia 0.6877732276916504
capital-common-countries Havana Cuba Hanoi Vietnam Viet_Nam 0.710931658744812
capital-common-countries Helsinki Finland Islamabad Pakistan Pakistan 0.7291182279586792
capital-common-countries Helsinki Finland Kabul Afghanistan Afghan 0.6359644532203674
capital-common-countries Helsinki Finland London England Britain 0.6623522639274597
capital-common-countries Helsinki Finland Madrid Spain Spain 0.7539469003677368
capital-common-countries Helsinki Finland Moscow Russia Russia 0.7918932437896729
capital-common-countries Helsinki Finland Oslo Norway Norway 0.7523171305656433
capital-common-countries Helsinki Finland Ottawa Canada Canada 0.6696931719779968
capital-common-countries Helsinki Finland Paris France France 0.7549224495887756
capital-common-countries Helsinki Finland Rome Italy Italy 0.6867628693580627
capital-common-countries Helsinki Finland Stockholm Sweden Sweden 0.8256370425224304
capital-common-countries Helsinki Finland Tehran Iran Iran 0.7732710242271423
capital-common-countries Helsinki Finland Tokyo Japan Japan 0.8030251264572144
capital-common-countries Helsinki Finland Athens Greece Greece 0.6566227674484253
capital-common-countries Helsinki Finland Baghdad Iraq Mosul 0.6506971716880798
capital-common-countries Helsinki Finland Bangkok Thailand Thailand 0.752036452293396
capital-common-countries Helsinki Finland Beijing China China 0.7568843960762024
capital-common-countries Helsinki Finland Berlin Germany Germany 0.7419473528862
capital-common-countries Helsinki Finland Bern Switzerland Switzerland 0.5047450661659241
capital-common-countries Helsinki Finland Cairo Egypt Egypt 0.7302724719047546
capital-common-countries Helsinki Finland Canberra Australia Australia 0.6987783312797546
capital-common-countries Helsinki Finland Hanoi Vietnam Viet_Nam 0.6931595802307129
capital-common-countries Helsinki Finland Havana Cuba Cuba 0.6899740695953369
capital-common-countries Islamabad Pakistan Kabul Afghanistan Afghan 0.7332905530929565
capital-common-countries Islamabad Pakistan London England Britain 0.6056548953056335
capital-common-countries Islamabad Pakistan Madrid Spain Spain 0.6914529204368591
capital-common-countries Islamabad Pakistan Moscow Russia Russia 0.831927478313446
capital-common-countries Islamabad Pakistan Oslo Norway Norway 0.6795673370361328
capital-common-countries Islamabad Pakistan Ottawa Canada Canada 0.6421677470207214
capital-common-countries Islamabad Pakistan Paris France France 0.6944429874420166
capital-common-countries Islamabad Pakistan Rome Italy Italy 0.6518086194992065
capital-common-countries Islamabad Pakistan Stockholm Sweden Sweden 0.7098783850669861
capital-common-countries Islamabad Pakistan Tehran Iran Iran 0.8605974316596985
capital-common-countries Islamabad Pakistan Tokyo Japan Japan 0.7747604250907898
capital-common-countries Islamabad Pakistan Athens Greece Greece 0.6418430805206299
capital-common-countries Islamabad Pakistan Baghdad Iraq Iraqi 0.7481118440628052
capital-common-countries Islamabad Pakistan Bangkok Thailand Thailand 0.7783142924308777
capital-common-countries Islamabad Pakistan Beijing China China 0.8079829812049866
capital-common-countries Islamabad Pakistan Berlin Germany Germany 0.7216539978981018
capital-common-countries Islamabad Pakistan Bern Switzerland Switzerland 0.49683260917663574
capital-common-countries Islamabad Pakistan Cairo Egypt Egypt 0.7879177927970886
capital-common-countries Islamabad Pakistan Canberra Australia Australia 0.7616326808929443
capital-common-countries Islamabad Pakistan Hanoi Vietnam Viet_Nam 0.7534359693527222
capital-common-countries Islamabad Pakistan Havana Cuba Cuba 0.795850396156311
capital-common-countries Islamabad Pakistan Helsinki Finland Finland 0.6935101747512817
capital-common-countries Kabul Afghanistan London England EURASIAN_NATURAL_RESOURCES_CORP. 0.5547584891319275
capital-common-countries Kabul Afghanistan Madrid Spain Spain 0.6156004667282104
capital-common-countries Kabul Afghanistan Moscow Russia Russia 0.7199913263320923
capital-common-countries Kabul Afghanistan Oslo Norway Norway 0.5757439136505127
capital-common-countries Kabul Afghanistan Ottawa Canada Ontario 0.551449179649353
capital-common-countries Kabul Afghanistan Paris France France 0.6088168621063232
capital-common-countries Kabul Afghanistan Rome Italy Italy 0.537543773651123
capital-common-countries Kabul Afghanistan Stockholm Sweden Sweden 0.5849065184593201
capital-common-countries Kabul Afghanistan Tehran Iran Iran 0.7807148694992065
capital-common-countries Kabul Afghanistan Tokyo Japan Japan 0.6695032119750977
capital-common-countries Kabul Afghanistan Athens Greece Greece 0.5494599342346191
capital-common-countries Kabul Afghanistan Baghdad Iraq Iraq 0.8607980608940125
capital-common-countries Kabul Afghanistan Bangkok Thailand Thailand 0.6891651749610901
capital-common-countries Kabul Afghanistan Beijing China China 0.6837893128395081
capital-common-countries Kabul Afghanistan Berlin Germany Germany 0.6105467677116394
capital-common-countries Kabul Afghanistan Bern Switzerland Bern_NC 0.4233846962451935
capital-common-countries Kabul Afghanistan Cairo Egypt Egypt 0.6705425977706909
capital-common-countries Kabul Afghanistan Canberra Australia Mr_Rudd 0.6034548282623291
capital-common-countries Kabul Afghanistan Hanoi Vietnam Vietnam 0.7514270544052124
capital-common-countries Kabul Afghanistan Havana Cuba Cuba 0.7205935716629028
capital-common-countries Kabul Afghanistan Helsinki Finland Finland 0.5768634080886841
capital-common-countries Kabul Afghanistan Islamabad Pakistan Pakistan 0.7463313341140747
capital-common-countries London England Madrid Spain Spain 0.6087852716445923
capital-common-countries London England Moscow Russia Russia 0.6502718329429626
capital-common-countries London England Oslo Norway Norway 0.5689430236816406
capital-common-countries London England Ottawa Canada Canada 0.5256192088127136
capital-common-countries London England Paris France France 0.6676377058029175
capital-common-countries London England Rome Italy Italy 0.5715967416763306
capital-common-countries London England Stockholm Sweden Sweden 0.6610991358757019
capital-common-countries London England Tehran Iran Iran 0.6443778872489929
capital-common-countries London England Tokyo Japan Japan 0.6889490485191345
capital-common-countries London England Athens Greece Greece 0.5293722748756409
capital-common-countries London England Baghdad Iraq Iraqi 0.5854012370109558
capital-common-countries London England Bangkok Thailand Thailand 0.6264095902442932
capital-common-countries London England Beijing China China 0.6181186437606812
capital-common-countries London England Berlin Germany Germany 0.5952338576316833
'''