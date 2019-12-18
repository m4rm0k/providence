import numpy
def glyph(char):
    quads = []
    if char == '0':
        quads += [ [0.057332119922423264,-0.12517747614738425,-0.28040612203433224,-0.1255870367491757,-0.33639470744287847,-0.05459341518340759],[-0.33639470744287847,-0.05459341518340759,-0.3923832928514247,0.016400206382360533,-0.15257230542096623,0.07706325990669327],[0.26642324258923933,0.03150432716249795,0.35576990392998575,-0.04525048530342283,0.09231619081298736,-0.11873654453733826] ]
    if char == '1':
        quads += [ [-0.5,0.09146138201253899,-0.19193799398066466,0.0991975398008053,0.03238806359155219,0.11036763633813379],[0.03238806359155219,0.11036763633813379,0.256714121163769,0.12153773287546228,0.39088210594366,0.145],[0.3761212173362734,-0.0019606233224382062,0.31567357688775943,-0.062186399672928716,0.2860724001955145,-0.13786158896437337] ]
    if char == '2':
        quads += [ [-0.16752570705612202,0.01868035344523214,-0.3453532912931352,0.016428103207451937,-0.3580904877863267,0.05495468222690841],[-0.3580904877863267,0.05495468222690841,-0.3708276842795182,0.09348126124636488,-0.17912364121612961,0.11787075647839784],[-0.17912364121612961,0.11787075647839784,0.16505435016362746,0.12347896628048478,0.19031927942637827,0.051152454931385885],[0.19031927942637827,0.051152454931385885,0.2155842086891291,-0.021174056417713014,-0.37628867652796893,-0.10357757802651252],[-0.37628867652796893,-0.10357757802651252,-0.35850306360708434,-0.10034670042750914,-0.4014486808843635,-0.10072221307755834],[-0.4014486808843635,-0.10072221307755834,-0.4443942981616426,-0.10109772572760754,-0.5,-0.10434625991202026],[-0.5,-0.10434625991202026,-0.335189032616163,-0.10057098229472392,-0.27585787000135426,-0.10342774270997987],[-0.27585787000135426,-0.10342774270997987,-0.2165267073865455,-0.10628450312523582,-0.13659777956829317,-0.11588002413130985],[0.15403545437287394,-0.1308368633060954,0.2214855166556613,-0.12687887188161387,0.28479380248002206,-0.11972466344986535] ]
    if char == '3':
        quads += [ [-0.19795403046180793,0.04320064736478306,-0.31142199119508324,0.06034016245045533,-0.2727790765076299,0.08356821584682561],[-0.2727790765076299,0.08356821584682561,-0.23413616182017657,0.1067962692431959,-0.11157582132787558,0.12028724036868703],[-0.11157582132787558,0.12028724036868703,0.15745668183943295,0.13041077896229836,0.2119060730061382,0.09422311761264685],[0.2119060730061382,0.09422311761264685,0.26635546417284345,0.05803545626299534,-0.10197832257280043,0.017712420792901112],[-0.10197832257280043,0.017712420792901112,0.3124518616976085,0.029607538460221662,0.3421880432926171,-0.020673787663192708],[0.3421880432926171,-0.020673787663192708,0.37192422488762567,-0.07095511378660707,0.057981358654471515,-0.10662082533700432],[0.057981358654471515,-0.10662082533700432,-0.3726931314286537,-0.12242581607999936,-0.3955488102281116,-0.0863742618680326],[-0.3955488102281116,-0.0863742618680326,-0.41840448902756955,-0.050322707656065835,-0.2267468148623356,-0.023317619018198843],[-0.04309769364258968,-0.02301450102906477,0.023575546628799765,-0.02972793329147427,-0.02199859000990223,-0.049427618902356585] ]
    if char == '4':
        quads += [ [0.14583334201122355,0.059546163849154746,0.1734537781347739,0.031612350887434235,0.16788810581917074,0.0067591757118972105],[0.16788810581917074,0.0067591757118972105,0.1623224335035676,-0.018093999463639817,0.1562499349158195,-0.0490034659377406],[0.1562499349158195,-0.0490034659377406,0.14782111800211153,-0.08392410866675004,0.14372169879499486,-0.11107876980441077],[0.14372169879499486,-0.11107876980441077,0.13962227958787818,-0.1382334309420715,0.17708332899438817,-0.14292572383960087],[0.05555564811972369,0.145,0.07514745199122924,0.09878588300377764,-0.031223016098806032,0.052577016931610064],[-0.031223016098806032,0.052577016931610064,-0.13759348418884132,0.006368150859442499,-0.38194437791394864,-0.015129778933680116],[-0.5,-0.016669631909981247,-0.3591129141805328,-0.013884558645012873,-0.3052330128206462,-0.0186571335686421],[-0.3052330128206462,-0.0186571335686421,-0.25135311146075956,-0.02342970849227133,-0.16666652782041552,-0.029756996894987037],[0.22082627647259973,-0.039218573020886,0.4013192037354363,-0.03524802757276953,0.5,-0.0074312836708156915] ]
    if char == '5':
        quads += [ [-0.3739649437907178,0.11474365425156688,-0.35641553679358945,0.11450873058285435,-0.35101945452845495,0.08535302092436042],[-0.35101945452845495,0.08535302092436042,-0.34562337226332046,0.0561973112658665,-0.3463518921466445,0.009535083242541598],[-0.3463518921466445,0.009535083242541598,-0.3129471906214627,0.02360734857813835,-0.2665318648714553,0.03349004611635781],[-0.2665318648714553,0.03349004611635781,-0.2201165391214479,0.043372743654577266,-0.17607115055224432,0.049748182711551556],[-0.17607115055224432,0.049748182711551556,0.20385126487335953,0.08077396998771808,0.2643957242052213,0.018761730611054635],[0.2643957242052213,0.018761730611054635,0.32494018353708304,-0.043250508765608806,-0.04951131219862742,-0.10783090874177628],[-0.04951131219862742,-0.10783090874177628,-0.30692539275428443,-0.1254914394394923,-0.3591053274107151,-0.09303091893337831],[-0.3591053274107151,-0.09303091893337831,-0.4112852620671458,-0.06057039842726431,-0.24740510543709987,-0.0334834947388743],[-0.24740510543709987,-0.0334834947388743,-0.20878009623636035,-0.029647256439246487,-0.16724440391137782,-0.02891366698978587],[-0.16724440391137782,-0.02891366698978587,-0.1257087115863953,-0.02818007754032525,-0.09093092630130084,-0.03395102485929444],[-0.04718988210939847,0.12517860269284203,0.12301943129784726,0.1227249935082809,0.2703401074828865,0.13485027843354308] ]
    if char == '6':
        quads += [ [0.38056000021298775,0.10527139775474365,0.29524104785533944,0.13558720182189718,0.15309710348848568,0.13517403271537903],[0.15309710348848568,0.13517403271537903,0.010953159121631917,0.1347608636088609,-0.10646433639415714,0.11495752606369401],[-0.10646433639415714,0.11495752606369401,-0.39373836672958024,0.03623337278710488,-0.3669784009616435,-0.023935756216247297],[-0.3669784009616435,-0.023935756216247297,-0.3402184351937068,-0.08410488521959948,-0.20679593298314464,-0.12206894804278298],[-0.20679593298314464,-0.12206894804278298,-0.11398932770276823,-0.1393037131150853,-0.019340277870221093,-0.1391624144765488],[-0.019340277870221093,-0.1391624144765488,0.07530877196232605,-0.13902111583801233,0.16317587265413036,-0.12320834313485038],[0.16317587265413036,-0.12320834313485038,0.3898503891051603,-0.06303347200724593,0.2725627284635268,-0.02757649093589048],[0.2725627284635268,-0.02757649093589048,0.15527506782189332,0.007880490135464976,-0.0751110868540788,-0.008113835654833063],[-0.21041532439491248,-0.056466234503175644,-0.22838287337538732,-0.08417940689406872,-0.13990820192381898,-0.09585923227843968] ]
    if char == '7':
        quads += [ [-0.42599208880949346,0.05547873296390593,-0.4792852126573629,0.07114339083913704,-0.4492814922646483,0.09266886254190612],[-0.4492814922646483,0.09266886254190612,-0.4192777718719337,0.1141943342446752,-0.3354615535436965,0.12878390801949277],[-0.3354615535436965,0.12878390801949277,-0.24005768773438307,0.14046100018157662,-0.1378934198937498,0.139140409528692],[-0.1378934198937498,0.139140409528692,-0.03572915205311657,0.13781981887580738,0.06545638730599435,0.13267129986981702],[0.06545638730599435,0.13267129986981702,0.19410575842002287,0.12651768941091499,0.29948092537898774,0.12906964493496598],[0.29948092537898774,0.12906964493496598,0.4048560923379526,0.13162160045901697,0.5,0.13766939897005778],[-0.06063229614368297,-0.006934778977200677,-0.16593384481843104,-0.08299350170961778,-0.18802771095211152,-0.145] ]
    if char == '8':
        quads += [ [0.09030988865158618,0.020304749371682085,0.3490383222365835,-0.03391267213108662,0.3117047698903107,-0.05932634425758267],[0.3117047698903107,-0.05932634425758267,0.2743712175440379,-0.08474001638407871,0.16647119352230078,-0.10410462120273115],[0.16647119352230078,-0.10410462120273115,-0.11253228542623822,-0.1285623238592022,-0.2028266874624171,-0.09002791564584234],[-0.2028266874624171,-0.09002791564584234,-0.293121089498596,-0.0514935074324825,0.07203174570261517,0.017428205608314568],[0.07203174570261517,0.017428205608314568,0.3747102313662552,0.07107073520037634,0.34343273412714886,0.09104421235432643],[0.34343273412714886,0.09104421235432643,0.31215523688804253,0.11101768950827652,0.22739984863250895,0.1303315540880885],[0.22739984863250895,0.1303315540880885,0.15523006519983007,0.1406778735925938,0.08767318812594688,0.1379266292093347],[0.08767318812594688,0.1379266292093347,0.02011631105206367,0.13517538482607563,-0.031547421568830225,0.12817422274497806],[-0.11690409093972218,0.0678502427562126,-0.03302033713692634,0.0423415652858322,0.11772839902958943,0.014551661844947272] ]
    if char == '9':
        quads += [ [0.4945661514011962,0.029635215148638663,0.4271324705944173,0.005195910556783747,0.34103902373670747,-0.0072616536105820344],[0.34103902373670747,-0.0072616536105820344,0.25494557687899766,-0.019719217777947814,0.17310979497177226,-0.02640526181952907],[0.17310979497177226,-0.02640526181952907,-0.3046364400022964,-0.04133159465743956,-0.3391156714004565,0.02059047568027915],[-0.3391156714004565,0.02059047568027915,-0.3735949027986166,0.08251254601799786,-0.07015310129447849,0.1252777838670854],[-0.07015310129447849,0.1252777838670854,0.14354108256287879,0.14053627209507694,0.3087357593620921,0.11309429755816323],[0.3087357593620921,0.11309429755816323,0.47393043616130537,0.08565232302124953,0.49022165962911735,0.013943805310704466],[0.49022165962911735,0.013943805310704466,0.4812089638317697,-0.037878098686133205,0.37550217594175106,-0.0686542489088569],[0.37550217594175106,-0.0686542489088569,0.2697953880517324,-0.09943039913158058,0.09926267451422155,-0.11980626867438451],[-0.1645941706936248,-0.1342180262477174,-0.31174071087015565,-0.1338015565789141,-0.43504883164401764,-0.10859814149456462] ]
    if char == 'a':
        quads += [ [0.3209073103251818,0.06881998441929102,-0.264087555372245,-0.0425738761660064,-0.1607643048426059,0.01623668858485196],[-0.1607643048426059,0.01623668858485196,-0.057441054312966824,0.07504725333571031,0.28508871100584643,0.06107352425952467],[0.31532922295396143,-0.005196469752322762,0.3392312245626184,-0.03755623424597616,0.5,-0.019833780254086164] ]
    if char == 'b':
        quads += [ [0.1892821443948841,0.11141056869880461,-0.028198896909967214,0.14063315955816627,-0.19683122278028742,0.08277134445862824],[-0.19683122278028742,0.08277134445862824,-0.3654635486506076,0.02490952935909021,-0.21219532607860353,-0.1421588628883738],[0.05614559197249409,-0.03580848963889355,0.16472481229035232,-0.06983812197409099,-0.2352308221103287,-0.145] ]
    if char == 'c':
        quads += [ [0.4789019684634136,-0.057501678799459,-0.06317022006210313,-0.10117971761410421,-0.20418025092049533,-0.036505789778426556],[-0.20418025092049533,-0.036505789778426556,-0.34519028177888755,0.028168138057251102,-0.12675159160420413,0.0907793247678145],[0.3054901170723076,0.09692017599230578,0.3917939609375489,0.07619803367851587,0.3311816347828954,0.057343415618227145] ]
    if char == 'd':
        quads += [ [-0.07142841745197803,0.1219661444283697,0.14073782727265824,0.13251414958463625,0.16241806559021033,0.08535944230703198],[0.16241806559021033,0.08535944230703198,0.1840983039077624,0.038204735029427714,0.17115908775397048,-0.03376768264245911],[0.17115908775397048,-0.03376768264245911,0.1673637042053453,-0.0996710933286758,0.26257553206303863,-0.12111225666816172],[0.26257553206303863,-0.12111225666816172,0.35778735992073196,-0.14255342000764765,0.5,-0.1378471981777347],[0.2304583994046896,-0.029912865789077314,0.19984306864985463,-0.052139965367561464,0.12924201280296901,-0.06625691710519034],[0.12924201280296901,-0.06625691710519034,0.05864095695608339,-0.08037386884281922,-0.022911024194403884,-0.09004771891002139],[-0.022911024194403884,-0.09004771891002139,-0.38786720112816925,-0.10630035089226453,-0.4018526171155209,-0.0759516054583341],[-0.4018526171155209,-0.0759516054583341,-0.41583803310287254,-0.04560286002440367,-0.2223718258803119,-0.018348476886764276],[0.00010578961845462281,-0.008925869133589507,0.09686524967608709,-0.010221155532888566,0.16037749271167223,-0.016035522034011124] ]
    if char == 'e':
        quads += [ [0.5,-0.05074957504686731,0.44798412904192275,-0.06863032501135709,0.38576245929542696,-0.08267332574711511],[0.38576245929542696,-0.08267332574711511,0.3235407895489312,-0.09671632648287314,0.27752021655029224,-0.10301393385048369],[0.27752021655029224,-0.10301393385048369,-0.05951865502721623,-0.11769786742086202,-0.18289091435980245,-0.0420211291369872],[-0.18289091435980245,-0.0420211291369872,-0.30626317369238865,0.03365560914688764,0.02886652563161507,0.11127000690879146],[0.02886652563161507,0.11127000690879146,0.22761389550593944,0.13280696788414384,0.31448067244151506,0.10677364573514248],[0.31448067244151506,0.10677364573514248,0.40134744937709066,0.08074032358614112,0.2448025705535023,0.031131300188430272],[0.05187855940152819,0.01340177219749527,-0.05166124375491937,0.015672535780946642,-0.11509101209002881,0.04506847414680265] ]
    if char == 'f':
        quads += [ [0.5,0.12925490072587925,0.4572676319155933,0.1401469394310791,0.3823226678796279,0.14170242344540754],[0.3823226678796279,0.14170242344540754,0.3073777038436625,0.143257907459736,0.22549028832233675,0.13850701752468592],[0.22549028832233675,0.13850701752468592,0.023424175234084233,0.0902079055548484,0.04489100843476531,0.06960227445970063],[0.04489100843476531,0.06960227445970063,0.06635784163544639,0.04899664336455286,0.11764709629761638,0.0015756395728525052],[0.11764709629761638,0.0015756395728525052,0.18183490497311194,-0.039374270074586236,0.16668493312198657,-0.0706616346187253],[0.16668493312198657,-0.0706616346187253,0.1515349612708612,-0.10194899916286435,-0.08333321082189588,-0.1279540326075618],[-0.3452037115281006,-0.13818873745537114,-0.45263038209591533,-0.13568662227718867,-0.5,-0.12055232683614267] ]
    if char == 'g':
        quads += [ [0.5,0.12847238328468427,0.4456525438931004,0.10498707067667006,0.3987854729487692,0.09325512173385778],[0.3987854729487692,0.09325512173385778,0.351918402004438,0.0815231727910455,0.27415849034320394,0.07487869243777921],[0.27415849034320394,0.07487869243777921,-0.046872905768180435,0.05750733217172049,-0.06205329094396102,0.08442327377570333],[-0.06205329094396102,0.08442327377570333,-0.0772336761197416,0.11133921537968616,0.10974057495724221,0.1356098747666386],[0.10974057495724221,0.1356098747666386,0.17849669247916727,0.14128748834273927,0.25900104772147764,0.14241894079347392],[0.25900104772147764,0.14241894079347392,0.339505402963788,0.14355039324420857,0.416859631808182,0.1399121254393256],[0.416859631808182,0.1399121254393256,0.46199060076611875,0.029784260781901897,0.4114700453911333,-0.02680985425411491],[0.4114700453911333,-0.02680985425411491,0.36094949001614784,-0.08340396929013172,0.08670676781180864,-0.11822338631143506],[-0.2888918836538509,-0.12859339354115587,-0.4521779202494396,-0.1200078411485808,-0.5,-0.09752670927734466] ]
    if char == 'h':
        quads += [ [0.2157423875687029,0.13660558479332682,0.18109351332780943,0.14311903697480555,0.08347670719720833,0.1423348681395658],[0.08347670719720833,0.1423348681395658,-0.014140098933392756,0.14155069930432607,-0.08941681488118314,0.13346624061902732],[-0.08941681488118314,0.13346624061902732,-0.39150231646022177,0.026309899316527597,-0.3896949678385643,0.00543791834740082],[-0.3896949678385643,0.00543791834740082,-0.3878876192169068,-0.015434062621725957,-0.3820357319568328,-0.07310322368505351],[-0.3820357319568328,-0.07310322368505351,-0.35335902239148825,-0.040426125949965294,-0.26214610301688956,-0.01265549689459547],[-0.26214610301688956,-0.01265549689459547,-0.17093318364229088,0.015115132160774352,-0.047614470640152506,0.01417079794239351],[0.1473049962222021,-0.09264826203964363,0.24592888997428386,-0.13043850981341715,0.5,-0.11705418021441136] ]
    if char == 'i':
        quads += [ [-0.5,0.02867742582871774,-0.021925150553435465,0.04547239708989009,0.0004684841499452974,0.01891100722445778],[0.0004684841499452974,0.01891100722445778,0.02286211885332606,-0.007650382640974531,0.009804844008497238,-0.05927384067150254],[0.09250650781329545,-0.12306733810693155,0.19178747114608508,-0.14153459218629194,0.5,-0.13587652737798392] ]
    if char == 'j':
        quads += [ [0.0091890817852609,0.145,0.030292391495827773,0.1384923275452616,0.05508464970271998,0.13536278026585108],[0.05508464970271998,0.13536278026585108,0.07987690790961219,0.13223323298644055,0.10803630425752242,0.13191848655790234],[0.08510877341777257,0.09577216964325193,0.15179204909649507,-0.05781873692273089,0.10065408406227924,-0.07273021884208361],[0.10065408406227924,-0.07273021884208361,0.049516119028063424,-0.08764170076143633,-0.050988852283251396,-0.11177965727007208],[-0.050988852283251396,-0.11177965727007208,-0.23886736111219892,-0.13568637164949474,-0.31563102384433867,-0.12031442538510954],[-0.31563102384433867,-0.12031442538510954,-0.3923946865764784,-0.10494247912072434,-0.21324717339803728,-0.05968738702890236],[0.16788018688211265,-0.03227699180236203,0.37979239353530864,-0.030074751801001356,0.32345281173300733,-0.07380584185736838] ]
    if char == 'k':
        quads += [ [-0.29553813035107757,-0.07410275559869689,-0.1064565342184343,-0.08619043173580668,0.07531564069690148,-0.09790808013196967],[0.07531564069690148,-0.09790808013196967,0.25708781561223726,-0.10962572852813265,0.5,-0.09567812316129484],[-0.5,-0.08163702449049323,-0.4007733873282021,-0.0612491048746656,-0.29664643607915964,-0.04484169794091786],[-0.29664643607915964,-0.04484169794091786,-0.19251948483011716,-0.028434291007170112,-0.06877252946471119,-0.019993135649434557],[-0.06877252946471119,-0.019993135649434557,0.16525559996595932,-0.00897635556730781,0.15178575189960417,-0.025109152619832823],[0.15178575189960417,-0.025109152619832823,0.13831590383324902,-0.041241949672357836,-0.17286128941208057,-0.06554109933992855],[-0.17286128941208057,-0.06554109933992855,-0.26273923316481795,-0.07155242100673041,-0.2983334690776718,-0.07400005955230055],[-0.2983334690776718,-0.07400005955230055,-0.3339277049905256,-0.07644769809787068,-0.37732315906100294,-0.07889729034802187],[-0.3526437848517707,0.041777237761333116,-0.43171077765195487,-0.036183248054767775,-0.42522640049541705,-0.145] ]
    if char == 'l':
        quads += [ [-0.5,0.10920384937194455,0.14659403122550232,0.1364594277274989,0.14443637710544313,0.10729669884051639],[0.14443637710544313,0.10729669884051639,0.14227872298538394,0.07813396995353389,0.1153840238491336,-0.0003455682744398225],[0.05271115992812466,-0.10558409076279665,0.0640710184259835,-0.13601656705687168,0.5,-0.1374590387762921] ]
    if char == 'm':
        quads += [ [-0.5,0.030139195263243684,-0.3578225430689652,0.05879620641621507,-0.3356831071651277,0.020076955297709885],[-0.3356831071651277,0.020076955297709885,-0.31354367126129024,-0.018642295820795303,-0.2986796131880316,-0.08474039408951684],[-0.2986796131880316,-0.08474039408951684,-0.2062402991874226,0.04648672503587799,-0.08491024207091587,0.04189763931498866],[-0.08491024207091587,0.04189763931498866,0.03641981504559086,0.037308553594099333,0.04125433447819582,-0.05891473423651761],[0.04125433447819582,-0.05891473423651761,0.08643779137902653,0.02239314165946285,0.18595167159914544,0.049400486478269126],[0.18595167159914544,0.049400486478269126,0.28546555181926436,0.0764078312970754,0.3151814789520049,-0.043775580109710305],[0.34806198097613616,-0.10793661277302316,0.38511606599372805,-0.1357758577176018,0.5,-0.12926735883939747] ]
    if char == 'n':
        quads += [ [-0.5,0.04925624773778109,-0.4572118485977035,0.05573150630275943,-0.42345404710638473,0.060684281656044184],[-0.42345404710638473,0.060684281656044184,-0.389696245615066,0.06563705700932894,-0.3571428571428576,0.06972889675707533],[-0.3571428571428576,0.06972889675707533,-0.29240242492977886,0.022975103340991898,-0.27322994023816827,-0.012552025188116607],[-0.27322994023816827,-0.012552025188116607,-0.2540574555465577,-0.04807915371722511,-0.25274750626181053,-0.11452507233145523],[-0.25274750626181053,-0.11452507233145523,-0.15700350567072777,0.013417616858332676,0.012460589049521624,0.048403196178291426],[0.012460589049521624,0.048403196178291426,0.18192468376977103,0.08338877549825018,0.23076855473041236,-0.026236711077243624],[0.24474969240233735,-0.09283667230139078,0.27972856521736544,-0.13158061230577628,0.5,-0.13499772135074942] ]
    if char == 'o':
        quads += [ [0.03951937881413037,-0.11347364936795948,-0.25809330470189473,-0.12453327811703274,-0.3248386348199399,-0.058993887408442296],[-0.3248386348199399,-0.058993887408442296,-0.3915839649379851,0.0065455033001481575,-0.16557266876040522,0.07486608845404971],[0.23570069350197959,0.05200141521293044,0.3492722380629069,-0.01042288039193097,0.10104699960497943,-0.09794053527487409] ]
    if char == 'p':
        quads += [ [-0.0536336674510684,0.07830284101851309,0.03193227356802529,0.09953271908623376,0.0867918306720008,0.10948535838587495],[0.0867918306720008,0.10948535838587495,0.1416513877759763,0.11943799768551613,0.1969655058448232,0.12404835453142318],[0.1969655058448232,0.12404835453142318,0.40296340560965105,0.13061250112787742,0.412007648393236,0.09334567790625956],[0.412007648393236,0.09334567790625956,0.42105189117682096,0.05607885468464168,0.22533500953118502,0.03093801170569979],[0.22533500953118502,0.03093801170569979,0.1497343129073673,0.025755451459411657,0.09128960093054325,0.026758410087444076],[0.09128960093054325,0.026758410087444076,0.0328448889537192,0.027761368715476496,-0.011079128311571762,0.031342877078989834],[-0.2900478998304769,0.11959525631686324,-0.24199071090882102,0.12427236363200525,-0.19799740884492467,0.1276141868809082],[-0.19799740884492467,0.1276141868809082,-0.15400410678102833,0.13095601012981115,-0.1151012090481412,0.13093046691618718],[-0.1151012090481412,0.13093046691618718,0.010238356881844338,-0.03234656866140816,-0.045082248304674784,-0.07459548790494766],[-0.045082248304674784,-0.07459548790494766,-0.1004028534911939,-0.11684440714848716,-0.3704285384217749,-0.1403041282547232],[-0.4516958362655452,-0.14389744604186028,-0.4742589795247352,-0.14392533409404162,-0.49336409429917516,-0.14354274366639044] ]
    if char == 'q':
        quads += [ [0.03828763667989499,0.09454083218742936,-0.22159397651098994,0.025930006047236935,-0.33668625698133614,0.034682021544409254],[-0.33668625698133614,0.034682021544409254,-0.45177853745168234,0.04343403704158157,-0.48231210464184265,0.0730598835339968],[-0.48231210464184265,0.0730598835339968,-0.42451635981530467,0.11849750122537256,-0.2609259385719923,0.12570254116292817],[-0.2609259385719923,0.12570254116292817,-0.09733551732867993,0.13290758110048378,0.04611616261003404,0.11356676371468769],[0.11183429804579081,0.145,-0.018526579180758757,0.014974548213585195,0.03562140059027227,-0.059532262891845156],[0.03562140059027227,-0.059532262891845156,0.0897693803613033,-0.1340390739972755,0.3410880734623244,-0.1231996013277745],[0.40953023310484105,-0.11947907500407975,0.4442371793183675,-0.11740671096294436,0.5,-0.11115346528936002] ]
    if char == 'r':
        quads += [ [-0.5,0.04526628220915219,-0.3192103056668877,0.08182681098258303,-0.28681449629931205,0.011668876083092639],[-0.28681449629931205,0.011668876083092639,-0.2544186869317364,-0.05848905881639775,-0.20307156772358032,-0.145],[-0.20307156772358032,-0.145,-0.22469047583819135,-0.09195120517952762,-0.1952237429928096,-0.038745720543633046],[-0.1952237429928096,-0.038745720543633046,-0.16575701014742783,0.014459764092261539,0.006238892315226563,0.08897613679582633],[0.26195381772482107,0.11475052617392885,0.35392305019588743,0.09922682009788958,0.14740178108358537,0.041409559817595504] ]
    if char == 's':
        quads += [ [0.3564888896518107,0.08821387069765196,0.40708441269553075,0.12217881226472155,0.25719917284188665,0.1282135468612736],[0.25719917284188665,0.1282135468612736,0.10731393298824257,0.13424828145782564,-0.08783502593830722,0.11647476255631219],[-0.08783502593830722,0.11647476255631219,-0.23273180681553612,0.09193198567558064,-0.13319099949498148,0.06698632497124193],[-0.13319099949498148,0.06698632497124193,-0.03365019217442683,0.04204066426690323,0.11840361167276436,0.010049119707915222],[0.11840361167276436,0.010049119707915222,0.2774278743896802,-0.02045033280522758,0.33479221731083186,-0.047566852944404665],[0.33479221731083186,-0.047566852944404665,0.39215656023198353,-0.07468337308358175,0.21219464627818574,-0.11179594682465996],[-0.18917044156787577,-0.12761319602036886,-0.3770269060329281,-0.11645617668440193,-0.27119100411097974,-0.06236824069572208] ]
    if char == 't':
        quads += [ [-0.3761904435474508,0.10336910510638336,-0.0041459346823034295,0.11738189739426755,-0.01932301193499767,0.08002868295650847],[-0.01932301193499767,0.08002868295650847,-0.034500089187691915,0.042675468518749406,-0.07142870744117868,-0.01854495262893202],[-0.06926308750033786,-0.10188947458952924,-0.020844814569377132,-0.1337909060145866,0.33809510752313476,-0.1308595255619646] ]
    if char == 'u':
        quads += [ [-0.5,0.09215931364063663,-0.36928027112348905,0.11882369766806057,-0.33863981712274915,0.09947709722026182],[-0.33863981712274915,0.09947709722026182,-0.30799936312200926,0.08013049677246308,-0.33999973341508527,-0.062347571124598516],[-0.33999973341508527,-0.062347571124598516,-0.2120205555787335,-0.051506277517766645,-0.06583314450235231,-0.007733705966841245],[-0.06583314450235231,-0.007733705966841245,0.08035426657402889,0.03603886558408415,0.2333337776415242,0.09054981362776511],[0.26540844141130104,-0.10532942632393544,0.3277472735418985,-0.12813109742377812,0.5,-0.1041932521178261] ]
    if char == 'v':
        quads += [ [-0.5,-0.02651042954298849,-0.3898138085859993,0.0045540547848641165,-0.30211561744275406,-0.013834708103503315],[-0.30211561744275406,-0.013834708103503315,-0.21441742629950883,-0.03222347099187074,-0.08841984317444745,-0.145],[-0.08841984317444745,-0.145,0.1438864229892516,-0.07809415198555619,0.27210586084843763,-0.019491430433859775],[0.27210586084843763,-0.019491430433859775,0.4003252987076237,0.03911129111783665,0.2717121511516072,0.10133357740569277],[0.13874448009233023,0.12672947660309175,0.051930201849881535,0.13382972284225322,-0.07813041640136476,0.11068801389736246] ]
    if char == 'w':
        quads += [ [-0.5,0.009998991171134036,-0.3851045656428061,0.025064577117287587,-0.3537000522398148,-0.020041668201235444],[-0.3537000522398148,-0.020041668201235444,-0.32229553883682355,-0.06514791351975847,-0.28378360641105915,-0.12768628383819688],[-0.28378360641105915,-0.12768628383819688,-0.235062981886711,-0.09673574282168995,-0.19923804357955632,-0.0654682751418415],[-0.19923804357955632,-0.0654682751418415,-0.16341310527240166,-0.03420080746199305,-0.1093367512347892,0.0017543822546357835],[-0.1093367512347892,0.0017543822546357835,-0.07185439255333738,-0.05159056581075369,-0.034300754327175935,-0.08270828139528964],[-0.034300754327175935,-0.08270828139528964,0.003252883898985509,-0.1138259969798256,0.045454545454545636,-0.145],[0.21681549435534347,0.04079566640227782,0.3558782352851247,0.1128947410832011,0.5,0.08420066961632985] ]
    if char == 'x':
        quads += [ [-0.40469101657077633,-0.10312353228512042,-0.19187967037206946,-0.027797660319078134,-0.01844893605164776,0.025244563265304498],[-0.01844893605164776,0.025244563265304498,0.15498179826877392,0.07828678684968712,0.3428226843727926,0.145],[-0.5,0.11132923246081015,-0.3588208894948911,0.12535939882777886,-0.3014268712492284,0.10126030141102627],[-0.3014268712492284,0.10126030141102627,-0.2440328530035657,0.07716120399427367,-0.11785768304790367,0.00632854513346115],[0.18951412968444953,-0.11370119557020238,0.31684114034979843,-0.13547922473637228,0.5,-0.11033883760184152] ]
    if char == 'y':
        quads += [ [-0.2715944377745113,0.13475253869693948,-0.1274010776277242,0.14102860086347416,-0.0983907013555998,0.1252050933514114],[-0.0983907013555998,0.1252050933514114,-0.06938032508347539,0.10938158583934861,-0.07292551094480787,0.08242122241118763],[-0.07292551094480787,0.08242122241118763,-0.08027001840828607,0.0404977278401108,0.04711089396598265,0.044452803327801285],[0.04711089396598265,0.044452803327801285,0.17449180634025135,0.04840787881549177,0.4535484857602776,0.13741345278377431],[0.4535484857602776,0.13741345278377431,0.4880722951202525,-0.007685775807456642,0.4477374536621892,-0.049362081286000475],[0.4477374536621892,-0.049362081286000475,0.4074026122041259,-0.09103838676454432,0.1903109908868551,-0.11626045732043458],[-0.21099567828227642,-0.11520731109372902,-0.37227675325827814,-0.09471843824602702,-0.22192745432752814,-0.0488505864966437] ]
    if char == 'z':
        quads += [ [-0.5,0.08209146805512649,-0.3044009286980762,0.1261467029253903,-0.22974342182788277,0.12484067436247141],[-0.22974342182788277,0.12484067436247141,-0.15508591495768934,0.12353464579955253,-0.03140098018193366,0.11977830606898612],[-0.03140098018193366,0.11977830606898612,0.05593125016848964,0.11864740975374496,0.13541938322331912,0.118916333240401],[0.13541938322331912,0.118916333240401,0.21490751627814858,0.11918525672705704,0.25845392430152025,0.12354704010408438],[0.25845392430152025,0.12354704010408438,-0.03340878783360954,0.02111088419997057,-0.18852214971631753,-0.01102658242473118],[-0.18852214971631753,-0.01102658242473118,-0.3436355115990255,-0.04316404904943293,-0.4710147027290155,-0.046043831425708004],[-0.4710147027290155,-0.046043831425708004,-0.2922955448555913,-0.045131968004135554,-0.2130023094353603,-0.05712006673548681],[-0.2130023094353603,-0.05712006673548681,-0.13370907401512933,-0.06910816546683807,-0.04589314587401955,-0.08373066943956767],[0.22016858588375857,-0.11840034510560385,0.3548390905177023,-0.13011300615176827,0.5,-0.10257406332964134] ]
    if char == ',':
        quads += [ [0.08373188136813967,-0.037076212885600535,-0.12188356252666674,-0.11163447859848795,-0.5,-0.145] ]
    if char == '.':
        quads += [ [-0.08389155757646474,-0.017253540672341056,0.1412990209851738,-0.09253899027306058,0.5,-0.145] ]
    if char == '!':
        quads += [ [-0.11363987934101527,0.145,0.08211038175410075,0.1045363848948621,0.11590102676154772,0.08015976957068627],[0.11590102676154772,0.08015976957068627,0.14969167176899467,0.05578315424651044,-0.06819939670508313,0.019630752879302826],[-0.06819939670508313,0.019630752879302826,-0.12381351332723431,0.005832425556110106,-0.12143485575063823,-0.006034992251177155],[-0.12143485575063823,-0.006034992251177155,-0.11905619817404214,-0.017902410058464414,-0.02275891406915098,-0.034800022775256595],[-0.02275891406915098,-0.034800022775256595,0.031437676717812266,-0.04460796847525737,-0.04350805360043715,-0.05477268919497333],[-0.04350805360043715,-0.05477268919497333,-0.11845378391868656,-0.06493740991468928,-0.2954888235749116,-0.07093847146613746],[-0.10092862943769308,-0.13280394496241432,0.17404108615470248,-0.1382511730072328,0.5,-0.145] ]
    if char == '?':
        quads += [ [-0.11320621411903475,-0.08806102218190273,-0.3013402323819769,-0.06137948659127446,-0.21652245310746404,-0.03979261926187089],[-0.21652245310746404,-0.03979261926187089,-0.1317046738329512,-0.018205751932467314,0.09795655122853164,0.00378939019275068],[0.09795655122853164,0.00378939019275068,0.3583180129921948,0.030819626131487088,0.3924823824961444,0.06509112601935324],[0.3924823824961444,0.06509112601935324,0.42664675200009405,0.09936262590721939,0.22845022487424005,0.12473269416481325],[0.22845022487424005,0.12473269416481325,0.14049504631701576,0.13505632277069823,0.04136353726775799,0.1379169935973408],[0.04136353726775799,0.1379169935973408,-0.05776797178149977,0.14077766442398337,-0.1582860303438916,0.13138255857622191],[-0.1582860303438916,0.13138255857622191,-0.20106446716199683,0.12699167006108658,-0.23948185563638963,0.12096043163384226],[-0.23948185563638963,0.12096043163384226,-0.27789924411078243,0.11492919320659796,-0.331486632700025,0.10478327773225624],[-0.331486632700025,0.10478327773225624,-0.4285191196272354,0.081471221173952,-0.42965476051095297,0.04686205613635899],[-0.42965476051095297,0.04686205613635899,-0.43079040139467056,0.012252891098765976,-0.2745433882128762,0.0017112633637675623],[-0.2745433882128762,0.0017112633637675623,-0.20439814253043423,0.009872177107392487,-0.19235250954807173,0.013008978476530361],[-0.19235250954807173,0.013008978476530361,-0.18030687656570923,0.016145779845668236,-0.14642260208160113,0.02498561200202866],[-0.0896506879456106,-0.13071128683571337,-0.030554072490385775,-0.13720091899331327,0.029150887788965574,-0.145] ]
    return [ quads ]
def pack_length(char):
    gly = glyph(char)
    quads = gly[0]
    return 1 + len(quads)*6