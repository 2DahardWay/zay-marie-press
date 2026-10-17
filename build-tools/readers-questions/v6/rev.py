"""Publisher's revised text (attachment 3f5b1a2b, 2026-10-17). Overlays c1/c2 entries; tables (KJV, readings) are kept."""
import re
T={}
def add(n,title,sub,answer,stand,carry,other,means,related):
    T[n]=dict(title=f"{n}. {title}",sub=sub,answer=answer,stand=[stand],carry=carry,other=other,means=[means],related=related)
def tags(s):
    out=[]
    for m in re.finditer(r'(Stated|Shown|Inferred):\s*(.*?)(?=\s(?:Stated|Shown|Inferred):|$)',s):
        t={'Shown':'Shown by the context'}.get(m.group(1),m.group(1)); out.append((t,m.group(2).strip()))
    return out
def rd(lines): return [f"<b>{a}:</b> {b}" for a,b in (l.split(': ',1) for l in lines)]
add(1,"Why Did Jesus Cry “My God, My God, Why Hast Thou Forsaken Me?”","Matthew 27:46 &amp; Psalm 22:1",
"Jesus speaks the first line of Psalm 22 at the end of the darkness, and the forsaking is real in the hour of the cross. Matthew has already built the scene from Psalm 22 before the cry. The psalm itself turns from abandonment to being heard, and Hebrews places its praise in His mouth. The Gospels do not explain the forsaking; Paul gives that explanation to the Body.",
"Matthew records the crucifixion in order: garments parted, heads wagged, taunts spoken, darkness falling, and the cry at the ninth hour. Psalm 22 describes the mocked sufferer and the turning to praise. The setting is Israel’s, and Matthew uses the psalm’s details before the cry.",
tags("Stated: the cry is spoken with a loud voice at the ninth hour. Shown: Matthew has already used Psalm 22’s details. Inferred: the forsaking is real, not merely felt. Inferred: Paul’s explanation belongs to the Body and is not read back into the Gospels."),
rd(["Real abandonment: must explain Psalm 22:24 and John 16:32.","Quotation of the whole psalm: must explain the question “why” and the darkness.","Felt, not real: must explain why the Gospels record the cry at all."]),
"The cry belongs to the psalm’s scene and its answer. The reader does not build a doctrine of the Godhead on one line. The Body receives Paul’s explanation of the cross.",
"<b>Commentary Series:</b> Typology Commentary, Volume 1 (the rent veil). <b>Companions:</b> Psalms; Matthew; Mark.")
add(2,"What Does “Ye Are Gods” Mean in John 10:34 and Psalm 82:6?","Human judges, divine beings, or something else?",
"Psalm 82 addresses Israel’s judges, who stand in God’s place and judge unjustly. Jesus quotes the line to answer a charge of blasphemy: if Scripture calls those who received God’s word “gods,” He whom the Father sanctified does not blaspheme in saying He is the Son of God. His claim rests on His works and His oneness with the Father.",
"John 10 places the scene at the feast of dedication. The charge is blasphemy. Psalm 82 charges unjust judges and calls them “gods” who will die like men. Exodus 22 uses the same Hebrew word for human judges.",
tags("Stated: Jesus calls it “your law” and names those addressed as those who received God’s word. Shown: Psalm 82 addresses unjust judges who will die like men. Inferred: Jesus argues from lesser to greater."),
rd(["Heavenly council: strains at “die like men.”","Israel at Sinai: strains at the charge of unjust judging.","Human judges: fits the charge and the mortality."]),
"The verse does not teach that believers become gods. Jesus uses Scripture to silence a charge and then points to His works.",
"<b>Commentary Series:</b> Gospel Commentary, Volume 2 (The Lord’s Ministry to Israel); Volume 4 (What the Twelve Understood). <b>Companions:</b> Psalms; John.")
add(3,"Why Did Satan Quote Psalm 91 to Jesus?","Matthew 4:6 &amp; Psalm 91:11–12",
"Satan quotes Psalm 91 accurately but omits “in all thy ways,” turning a promise for the one who trusts God into a test of God. Jesus answers from Deuteronomy 6:16. The psalm is true; the use is false.",
"Matthew 4 records three temptations, each answered from Deuteronomy. Psalm 91 promises protection to the one who dwells with God. The devil quotes the promise without its condition.",
tags("Stated: Satan says “it is written”; Jesus says “it is written again.” Shown: the promise rests on trust and “thy ways.” Inferred: the omission is deliberate; the use is presumption."),
rd(["Misquotation: strains because the words are correct.","Unconditional promise: strains at “Thou shalt not tempt.”","Promise misused: fits the Lord’s answer."]),
"Psalm 91 is not doubted and not proved. Scripture must be used in its setting.",
"<b>Companions:</b> Psalms; Matthew; Luke.")
add(4,"What Does “What Is Man” Mean in Psalm 8 and Hebrews 2?","Dominion, the Son of Man, and the world to come",
"Psalm 8 marvels at man’s place over God’s works. Hebrews reads the psalm in light of the world to come: the rule is not yet seen, but Jesus is seen, made lower and crowned. Hebrews applies the psalm to the Son of man and to Israel’s hope.",
"Hebrews 2 speaks of the world to come and quotes Psalm 8. The readers are Hebrews. Psalm 8 speaks of man’s dominion.",
tags("Stated: the world to come is the subject. Shown: the rule is not yet seen; Jesus is. Inferred: Hebrews reads the psalm in Israel’s hope; Paul uses the same line differently for the Body."),
rd(["Christ alone: strains at the psalm’s “man.”","Humanity alone: strains at Hebrews’ “we see Jesus.”","Both in order: fits the text."]),
"The psalm’s wonder is fulfilled in Jesus and awaits the world to come.",
"<b>Companions:</b> Psalms; Hebrews; Matthew.")
add(5,"Should Believers Pray the Cursing Psalms?","Psalm 69, Psalm 109, and Acts 1:20",
"Psalm 69 and 109 are David’s prayers against enemies. Acts 1 quotes Psalm 69:25 and 109:8 in Israel’s setting. The Body is not told to pray these psalms as its own. They are Scripture, but their setting is Israel’s.",
"Psalm 69 and 109 speak of enemies and judgment. Acts 1 applies them to Judas in Israel’s program.",
tags("Stated: the psalms speak from David’s place. Shown: Acts uses them in Israel’s setting. Inferred: the Body is not given these prayers as its own."),
rd(["For all believers: strains at Israel’s setting.","Never for believers: strains at their place in Scripture.","For Israel’s setting: fits Acts 1."]),
"The psalms are Scripture; their use belongs to their setting.",
"<b>Commentary Series:</b> Acts Commentary, Volume 1 (Acts 1–8). <b>Companions:</b> Psalms; Acts.")
add(6,"Does “Be Ye Angry, and Sin Not” Permit Anger?","Psalm 4:4 &amp; Ephesians 4:26",
"Psalm 4:4 commands trembling and reflection. Paul quotes it to the Body and warns against sinning in anger. The psalm’s command is inward; Paul’s warning is practical.",
"Psalm 4 speaks of trembling before God. Ephesians 4 warns the Body about anger and its danger.",
tags("Stated: the psalm commands trembling. Shown: Paul warns against anger’s danger. Inferred: anger is not commended; restraint is commanded."),
rd(["Anger permitted: strains at Paul’s warning.","Anger forbidden: strains at Paul’s quotation.","Anger restrained: fits both."]),
"Anger is not a virtue; restraint is.",
"<b>Companions:</b> Psalms; Ephesians.")
add(7,"Why Does Paul Say Christ “Gave Gifts” When Psalm 68 Says “Received”?","Ephesians 4:8 &amp; Psalm 68:18",
"Psalm 68 speaks of the victor receiving gifts. Paul applies the victory to Christ and states the result for the Body: He gave gifts. The psalm’s movement is upward; Paul’s application is downward.",
"Psalm 68 celebrates God’s victory. Ephesians 4 applies the victory to Christ’s ascension.",
tags("Stated: the psalm says “received.” Shown: Paul applies the victory to Christ’s giving. Inferred: the psalm’s movement allows Paul’s application."),
rd(["Contradiction: strains at Paul’s argument.","Different gifts: strains at the psalm’s movement.","Application: fits both."]),
"Christ’s victory results in gifts for the Body.",
"<b>Commentary Series:</b> Prophecy &amp; Mystery Commentary, Volume 2 (The Mystery Program); Pauline Doctrine Series, Volume 4 (The Assembly in Order). <b>Companions:</b> Psalms; Ephesians.")
add(8,"Does “A Thousand Years Is as One Day” Explain the Delay?","Psalm 90:4 &amp; 2 Peter 3:8",
"Psalm 90 speaks of God’s eternity. Peter quotes it to answer scoffers and to show that delay does not deny promise. The psalm does not give a formula; Peter uses it to correct a charge.",
"Psalm 90 contrasts God’s eternity with man’s brevity. 2 Peter 3 answers scoffers about the promise.",
tags("Stated: the psalm speaks of God’s eternity. Shown: Peter answers scoffers. Inferred: the psalm is not a timetable."),
rd(["Prophetic formula: strains at the psalm’s meaning.","No relevance: strains at Peter’s use.","Corrective use: fits both."]),
"God’s time is not man’s; delay is not denial.",
"<b>Commentary Series:</b> Prophecy &amp; Mystery Commentary, Volume 3 (The Kingdom Program). <b>Companions:</b> Psalms; 2 Peter.")
add(9,"What Is the “Rest” in Psalm 95 and Hebrews 3–4?","Israel’s rest, the warning, and the promise",
"Psalm 95 warns Israel not to repeat the wilderness refusal. Hebrews applies the warning to Hebrew believers and speaks of a rest still open. The rest is Israel’s promised rest; the warning is present.",
"Psalm 95 recalls Meribah. Hebrews warns its readers and speaks of a rest remaining.",
tags("Stated: the psalm warns Israel. Shown: Hebrews applies the warning to Hebrews. Inferred: the rest is Israel’s promised rest."),
rd(["Heaven: strains at the psalm’s warning.","Salvation: strains at the context.","Israel’s rest: fits both."]),
"The warning stands; the rest is God’s.",
"<b>Companions:</b> Psalms; Hebrews.")
add(10,"What Does “This Day Have I Begotten Thee” Mean?","Psalm 2:7, Acts 13:33, and Hebrews 1:5",
"Psalm 2 speaks of the king God sets on Zion. Acts 13 applies the line to the resurrection; Hebrews applies it to sonship. The psalm’s line is used in two settings without merging them.",
"Psalm 2 speaks of God’s king. Acts 13 applies the line to resurrection. Hebrews 1 applies it to sonship.",
tags("Stated: the psalm speaks of God’s king. Shown: Acts applies it to resurrection; Hebrews to sonship. Inferred: the line is used in two settings."),
rd(["Only resurrection: strains at Hebrews.","Only sonship: strains at Acts.","Two uses: fits both."]),
"The psalm’s line is true in both settings without merging them.",
"<b>Companions:</b> Psalms; Acts; Hebrews.")
def apply(E):
    for i,e in enumerate(E,1): e.update(T[i])
