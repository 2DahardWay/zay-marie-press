"""Volume 6 entries 1-5. Each entry is a dict; text uses <b>, <i> only. KJV quotations use curly quotes and are checked by chk.py."""
import kjvlib
def K(ref):
    t=kjvlib.text(ref)
    return '“'+t+'”'

ENTRIES=[]

# ---------------------------------------------------------------- 1
ENTRIES.append(dict(
title="1. Why Did Jesus Cry “My God, My God, Why Hast Thou Forsaken Me?” Matthew 27:46",
answer="Jesus spoke the first line of Psalm 22 in his own voice at the end of the three hours of darkness, and the forsaking was real in the hour of the cross. The cry is not the end of the psalm. The psalm turns from the cry to “thou hast heard me” (22:21) and ends in praise, and Matthew has already built the scene from it (27:35, 39, 43). The Gospels do not say why he was forsaken. Paul says it to the Body, in 2 Corinthians 5:21 and Galatians 3:13.",
stand=[
"Matthew 27 tells the crucifixion in order: the soldiers part his garments, the passers-by wag their heads, the chief priests say “He trusted in God; let him deliver him now,” and then the darkness comes “from the sixth hour … unto the ninth hour.” At the ninth hour he cries out. Mark gives the same cry in its Aramaic form, “Eloi, Eloi” (15:34). Psalm 22 is David’s psalm of one who is mocked, pierced and left, and who is then heard and praised among “the great congregation.”",
"The setting is Israel’s: the mockers are the chief priests, scribes and elders, the charge on the cross is “the King of Israel,” and the psalm closes with “the seed of Jacob” and “the seed of Israel” (22:23).",
],
rows=[
("Ps 22:1–2","Ps 22:1–2","The question “why”; the sufferer says “thou hearest not.”"),
("Ps 22:7–8, 18","Ps 22:7–8; Ps 22:18","“They shake the head”; “He trusted on the LORD”; “They part my garments.”"),
("Mt 27:35","Matt 27:35","The garments are parted, as in Psalm 22:18."),
("Mt 27:39–43","Matt 27:39–43","Heads wagged and “He trusted in God,” as in Psalm 22:7–8."),
("Mt 27:45–47","Matt 27:45–47","Darkness, the cry in Aramaic with its meaning, and the bystanders hearing “Elias.”"),
("Ps 22:21, 24","Ps 22:21; Ps 22:24","“Thou hast heard me”; “when he cried unto him, he heard.”"),
("Lk 23:46","Luke 23:46","Luke records a different word at the same hour: “Father, into thy hands I commend my spirit.”"),
("Heb 2:10–12","Heb 2:10–12","Hebrews puts Psalm 22:22 in his mouth: “I will declare thy name unto my brethren.”"),
],
carry=[
("Stated","the cry is spoken “with a loud voice” at the ninth hour, after the darkness, and its words are the first line of Psalm 22 (Matthew 27:45–46; Mark 15:33–34)."),
("Stated","the bystanders mishear it as a call for Elias, and he “cried again with a loud voice” and “yielded up the ghost” (Matthew 27:47–50). Luke and John record other words from the same hours (Luke 23:46; John 19:30); none of them contradicts another."),
("Shown by the context","Matthew has already built the scene from the psalm before the cry: the parted garments (27:35; Psalm 22:18), the wagging heads (27:39; Psalm 22:7) and the taunt “He trusted in God; let him deliver him” (27:43; Psalm 22:8). The cry belongs to a scene the psalm describes."),
("Shown by the context","the psalm does not end with the cry. It says “when he cried unto him, he heard” (22:24), and Hebrews 2:12 puts the second half of the psalm in his mouth."),
("Inferred","that the forsaking was real and not only a recital. The question is asked, and the darkness comes before it. No Gospel says the Father only seemed absent. The text does not describe what the forsaking was or how it stands to the Son’s person, and nothing here divides the Godhead."),
("Inferred","that the forsaking belongs to the judgment of the cross. The Gospels do not give the reason. Paul tells the Body that God “made him to be sin for us” and that he was “made a curse for us” (2 Corinthians 5:21; Galatians 3:13). That is Paul’s explanation to the Body, and it is not read back into what the Twelve understood at the cross."),
],
other=[
"<b>A real abandonment.</b> Many commentaries read the cry as the lowest point of the Son’s suffering, when the Father turned away. It must explain why the psalm itself says “neither hath he hid his face from him,” and John 16:32, “I am not alone, because the Father is with me.”",
"<b>Only a quotation of the whole psalm.</b> Some read the cry as pointing to Psalm 22 as a whole, which ends in vindication, so that no forsaking is meant. It must explain the question “why,” the darkness, and why Matthew and Mark keep the Aramaic words.",
"<b>Felt, not real.</b> Some read the words as how it felt to the Son as a man, with no change in the Father’s presence. It must explain why the Gospels record the cry at all, and why “forsaken” is asked as a question and answered by no Gospel. That is the weakest of the three on the text.",
],
rtbl=[
("A real abandonment","The Father turned away at the cross.","Psalm 22:24; John 16:32."),
("Quotation of the whole psalm","The cry points to the vindication.","“Why”; the darkness; the Aramaic kept."),
("Felt, not real","The Son felt forsaken; the Father did not leave.","“Forsaken” is asked as a real question."),
],
means=[
"The cry shows that the one mocked at the cross stood in the place the psalm describes, and that the psalm’s answer followed: he was heard. The reader does not need to explain the cry away, and does not need to build a doctrine of the Godhead on one line. The Body is given the explanation in Paul’s letters: Christ was made sin and a curse for it. The cry is the Lord’s, spoken once; the Body’s part is to believe what Paul says the cross did.",
],
related="<b>Companions:</b> Psalms; Matthew; Mark. <b>Commentary Series:</b> Typology Commentary, Volume 1 (Tabernacle &amp; Temple Typology) reads the rent veil of Matthew 27:51.",
))

# ---------------------------------------------------------------- 2
ENTRIES.append(dict(
title="2. What Does “Ye Are Gods” Mean in John 10:34 and Psalm 82:6?",
answer="The “gods” are the judges of Israel, addressed in Psalm 82 as men who stand in God’s place and judge unjustly. Jesus quotes the line to answer a charge of blasphemy: if Scripture calls those “unto whom the word of God came” gods, he whom the Father sanctified and sent does not blaspheme in saying “I am the Son of God.” He does not say that men become gods, and he does not rest his claim on the psalm. The psalm answers the charge; his works and his oneness with the Father carry the claim (10:30, 37–38).",
stand=[
"John 10:22 sets the scene at Jerusalem at the feast of the dedication, in winter, in Solomon’s porch. The Jews ask him to say plainly if he is the Christ. He points to his works, says “I and my Father are one,” and they take up stones. When he asks which work they stone him for, they answer that it is for blasphemy, “because that thou, being a man, makest thyself God.” He answers from “your law.” The setting is Israel’s: a feast, the temple, and Israel’s rulers.",
"Psalm 82 opens with God standing “in the congregation of the mighty” and judging “among the gods.” It then charges those addressed with unjust judging, tells them to defend the poor, says “Ye are gods,” and says they “shall die like men.” This is a different text from Genesis 6:1–4 and Job 1:6, where “the sons of God” are the subject of Volume 2, entry 9; this entry does not settle the two together.",
],
rows=[
("Ps 82:1–4","Ps 82:1–4","God judges “among the gods”; the charge is unjust judging; the duty is to defend the poor."),
("Ps 82:6–8","Ps 82:6–8","“Ye are gods … children of the most High. But ye shall die like men.”"),
("Ex 22:8–9","Exod 22:8–9","The KJV has the matter come “unto the judges.” The Hebrew word is the one the KJV translates <i>gods</i> in Psalm 82:1."),
("Jn 10:30–33","John 10:30–33","“I and my Father are one”; the charge: “makest thyself God.”"),
("Jn 10:34–36","John 10:34–36","“Is it not written in your law, I said, Ye are gods?” Those “unto whom the word of God came.”"),
("Jn 10:37–38","John 10:37–38","His own answer: “believe the works.”"),
],
carry=[
("Stated","Jesus calls it “your law” and names those addressed as those “unto whom the word of God came,” and he adds “the scripture cannot be broken” (John 10:34–35)."),
("Stated","the psalm addresses those who “judge unjustly” and says they “shall die like men” (Psalm 82:2, 7). The ones addressed are charged as judges and are mortal."),
("Shown by the context","in Exodus 22:8–9 the same Hebrew word is used of the men who judge a dispute, so in Israel’s law the word can name human judges who stand in God’s place."),
("Stated","Jesus does not rest the claim on the psalm. He ends with his works and the Father in him, “and I in him” (John 10:38). The quotation answers the charge that he made himself God."),
("Inferred","that the argument is from the lesser to the greater. If the word is used of men who received God’s word, it cannot be blasphemy for him whom the Father “sanctified, and sent into the world” to say he is the Son of God. The text states the premise and the question and leaves the inference to the hearers."),
("Inferred","that the “gods” are men, not beings in God’s heavenly court. Both readings fit Psalm 82:1; the phrase “unto whom the word of God came” and the verdict “die like men” favour men."),
],
other=[
"<b>Beings in God’s heavenly council.</b> Michael S. Heiser (<i>The Unseen Realm</i>) argues that the “gods” are divine beings in God’s heavenly council and that Jesus’s quotation supports his claim to deity. It must explain “unto whom the word of God came” and why the psalm says “die like men.”",
"<b>Israel at Sinai.</b> Jerome H. Neyrey (“I Said: You Are Gods”) argues that the “gods” are Israel at Sinai, which received the Torah, and that Jesus’s use answers the charge without explaining his claim. It must explain why Psalm 82 itself speaks of unjust judging.",
"<b>The judges of Israel.</b> Many commentaries read the “gods” as the human judges and rulers of Israel, which is the reading taken here. It must explain “children of the most High” and why the psalm begins in heaven.",
],
rtbl=[
("A heavenly council","The “gods” are divine beings.","“Unto whom the word of God came”; “die like men.”"),
("Israel at Sinai","The “gods” are the nation that received the Torah.","The charge of unjust judging in verses 2–4."),
("Israel’s judges","The “gods” are rulers who judged in God’s place.","“Children of the most High”; the opening in heaven."),
],
means=[
"The verse is no proof that believers become gods, and it is no denial that Jesus is God. He uses an Israelite word for rulers to silence a charge and then points back to his works and his oneness with the Father. The reader keeps his claim where he put it, in John 10:30 and 10:38, and takes from the psalm the charge to judge justly.",
],
related="<b>Commentary Series:</b> Gospel Commentary, Volume 2 (The Lord’s Ministry to Israel) reads John 10; Gospel Commentary, Volume 4 (What the Twelve Understood). <b>Companions:</b> Psalms; John.",
))

# ---------------------------------------------------------------- 3
ENTRIES.append(dict(
title="3. Why Did Satan Quote Psalm 91 to Jesus in Matthew 4:6?",
answer="Satan quotes Psalm 91:11–12 as written, but he turns a promise made to the one who trusts God into a way to force God’s hand, and he leaves out “in all thy ways.” Jesus does not deny the psalm. He answers from Deuteronomy 6:16, “Thou shalt not tempt the LORD thy God,” and the exchange shows what the psalm does not promise. A true text used against its setting is still a misuse.",
stand=[
"Matthew 4 puts the testing in the wilderness after forty days of fasting. The tempter begins each time with “If thou be the Son of God,” and Jesus answers each time with “It is written,” from Deuteronomy 8, 6 and 6, the book Israel heard before entering the land. In the second temptation the devil places him on the pinnacle of the temple and says “it is written.” Luke gives the same three in a different order (Luke 4:1–13).",
"Psalm 91 opens with the one who “dwelleth in the secret place of the most High” and says “I will say of the LORD, He is my refuge.” The promise of angels follows the condition: “Because thou hast made the LORD … thy habitation” (91:9).",
],
rows=[
("Ps 91:1–2","Ps 91:1–2","The one who dwells in the secret place says “He is my refuge.”"),
("Ps 91:9–12","Ps 91:9–12","“Because thou hast made the LORD … thy habitation”; “to keep thee in all thy ways.”"),
("Mt 4:5–7","Matt 4:5–7","“It is written”; the quotation stops at the stone; “It is written again.”"),
("Lk 4:9–12","Luke 4:9–12","Luke gives the quotation with “to keep thee,” and the same answer."),
("Dt 6:16","Deut 6:16","“Ye shall not tempt the LORD your God, as ye tempted him in Massah.”"),
("Ex 17:7","Exod 17:7","Massah: “Is the LORD among us, or not?”"),
],
carry=[
("Stated","the devil says “it is written” and quotes Psalm 91:11–12, and Jesus answers “It is written again” (Matthew 4:6–7). Both sides use Scripture; the dispute is over what it permits."),
("Stated","the psalm’s promise rests on a condition: the one who has made the LORD his “habitation” (91:9), and the angels keep him “in all thy ways” (91:11)."),
("Shown by the context","Matthew gives the quotation without “in all thy ways”; Luke has “to keep thee” and also omits the phrase. The Lord’s answer treats the quotation as a way of putting God to the proof, which is what Deuteronomy 6:16 forbids."),
("Shown by the context","each answer comes from the part of Deuteronomy that recalls Israel’s testing in the wilderness (Deuteronomy 8:3; 6:13, 16), and the second names Massah, where Israel “tempted the LORD, saying, Is the LORD among us, or not?” (Exodus 17:7)."),
("Inferred","that the omission is deliberate. The Gospels do not say so; the devil’s words simply leave out the phrase that ties the promise to the way of trust."),
("Inferred","that Psalm 91 is not a promise of exemption from harm to anyone who recites it. The Lord’s refusal shows that the promise does not cover a leap taken to prove it."),
],
other=[
"<b>Satan misquotes the psalm.</b> Some commentaries say the devil altered the text. The words he quotes are in the psalm; the fault is the omission and the use. This reading must explain why the Lord does not correct the wording.",
"<b>A promise for every believer.</b> Some read Psalm 91 as an unconditional promise of protection and Matthew 4 as showing only that Satan mis-timed it. This reading must explain why the Lord calls the use a testing of God.",
"<b>A promise used to presume on God.</b> The reading taken here: the promise is real and the use is presumption, and Deuteronomy 6:16 names the sin.",
],
rtbl=[
("A misquotation","Satan changed the words.","The words are in the psalm."),
("An unconditional promise","Any believer may count on the angels.","“Because thou hast made the LORD … thy habitation”; “Thou shalt not tempt.”"),
("A promise used to presume","The promise stands; the leap is the sin.","None; it follows the Lord’s own answer."),
],
means=[
"The reader is not told to doubt Psalm 91, and is not told to prove it. The psalm is a statement of trust by one who dwells with God; it is not a bargain to be called in by a risk taken on purpose. The verse also shows that quoting Scripture is not the same as keeping it, and that the right answer to a misused verse is another verse read in its own place.",
],
related="<b>Companions:</b> Psalms; Matthew; Luke.",
))

# ---------------------------------------------------------------- 4
ENTRIES.append(dict(
title="4. What Does “What Is Man” Mean in Psalm 8:4 and Hebrews 2:6–8?",
answer="Psalm 8 is David’s wonder that God has set man over the works of his hands. Hebrews 2 quotes it and says that rule has not yet been seen: “now we see not yet all things put under him.” What is seen is Jesus, made a little lower than the angels for the suffering of death and crowned with glory. Hebrews reads the psalm of the Son of man and of “the world to come” (2:5), and it writes to Hebrew believers.",
stand=[
"Hebrews 1 sets the Son above the angels. Hebrews 2 warns the readers to heed what they heard from the Lord and confirmed by those who heard him (2:1–4), then states the subject: God has not put “the world to come, whereof we speak” in subjection to angels (2:5). The quotation of Psalm 8 follows, introduced only by “one in a certain place testified.” The audience is plain: Jesus “took on him the seed of Abraham” (2:16).",
"Psalm 8 begins and ends with “O LORD our Lord, how excellent is thy name in all the earth.” In the middle it asks “What is man?” and answers with dominion: “thou hast put all things under his feet.” Other writers quote the same psalm in other places: the Lord at the temple (Matthew 21:16, Psalm 8:2) and Paul (1 Corinthians 15:27; Ephesians 1:22, Psalm 8:6).",
],
rows=[
("Ps 8:3–6","Ps 8:3–6","“What is man … and the son of man”; “a little lower than the angels”; “all things under his feet.”"),
("Heb 2:5–8","Heb 2:5–8","“The world to come, whereof we speak”; the quotation; “now we see not yet all things put under him.”"),
("Heb 2:9","Heb 2:9","“But we see Jesus” made lower and crowned."),
("Heb 2:16","Heb 2:16","“The seed of Abraham.”"),
("Mt 21:15–16","Matt 21:15–16","The Lord quotes Psalm 8:2 to the chief priests about the children’s praise."),
("1 Cor 15:25–27","1Cor 15:25–27","Paul quotes “all things under his feet” of Christ’s reign, to the Body."),
],
carry=[
("Stated","Hebrews names the subject as “the world to come,” not the present world, and says it was not put in subjection to angels (2:5)."),
("Stated","“But now we see not yet all things put under him. But we see Jesus” (2:8–9). The psalm’s rule is not yet seen over all things; what is seen is Jesus, made lower and crowned, who tasted death “for every man.”"),
("Shown by the context","the quotation does not name David, and Hebrews does not say that Psalm 8 is about Christ alone. It reads the psalm’s “man” and “son of man” as the place where the rule is first seen in Jesus."),
("Shown by the context","the readers are Hebrews, “the seed of Abraham” (2:16), warned about a salvation “confirmed unto us by them that heard him” (2:3). The “world to come” is the age Israel was told to look for."),
("Inferred","that “the world to come” is the kingdom age of Israel’s hope. The text names it only as “whereof we speak”; the letter returns to it in 6:5 and 12:28."),
("Inferred","that Paul’s use in 1 Corinthians 15 and Ephesians 1 is a separate use. He quotes the same line of Christ’s rule in letters to the Body, and a shared line is not a shared audience."),
],
other=[
"<b>A psalm about humanity.</b> Many commentaries read Psalm 8 as about man in general and Hebrews as applying it to Christ as the representative man. It must explain “the world to come” and why Hebrews says the rule is not yet seen.",
"<b>A psalm about the Messiah only.</b> Some read Psalm 8 as a prophecy of Christ from the start. It must explain the psalm’s own question “What is man” and its mention of “babes and sucklings,” which Matthew 21 uses of children.",
"<b>Man’s appointed rule, seen first in Jesus.</b> The reading taken here: Psalm 8 states what God appointed for man, and Hebrews says it is seen first in the Son of man and not yet in all things.",
],
rtbl=[
("Humanity in general","The psalm is about every man.","“The world to come”; “not yet.”"),
("The Messiah only","The psalm is about Christ from the start.","“What is man”; “babes and sucklings.”"),
("Man’s rule, seen first in Jesus","The psalm states the appointment; Hebrews shows its first sight.","None; it joins both texts."),
],
means=[
"The psalm answers the reader’s sense of smallness with an appointment, and Hebrews answers the reader’s sight of a fallen world with a person: “we see Jesus.” It does not say that the Body now rules the world. It says that the rule God appointed for man is first seen in the Lord who tasted death and is crowned.",
],
related="<b>Digital Studies:</b> Study 82, The Kinsman-Redeemer, reports Hebrews 2 as written; this entry argues a position on one quotation. <b>Commentary Series:</b> Covenantal Commentary, Volume 4 (The Eternal Purpose of God). <b>Companions:</b> Hebrews; Psalms.",
))

# ---------------------------------------------------------------- 5
ENTRIES.append(dict(
title="5. Should Believers Pray the Cursing Psalms in Psalm 69, Psalm 109 and Acts 1:20?",
answer="No. The cursing psalms are David’s prayers against those who hate God’s anointed, and Peter applies two of them to Judas in Acts 1:20 as Scripture the Holy Ghost spoke by David. They belong to Israel’s line. The Body’s word is the other one: “Bless them which persecute you,” “avenge not yourselves,” give place to wrath. The psalms still teach what they teach: God judges, and the wronged hand the matter to him.",
stand=[
"Acts 1 stands in the opening chapters of Acts, in Jerusalem, before Paul’s calling. Peter stands among “men and brethren” and says that “this scripture must needs have been fulfilled, which the Holy Ghost by the mouth of David spake before concerning Judas.” He then quotes two psalms together: “Let his habitation be desolate” (Psalm 69:25) and “his bishoprick let another take” (Psalm 109:8).",
"Psalm 109 opens with David’s complaint that men speak against him “without a cause” and repay his love with hatred: “For my love they are my adversaries: but I give myself unto prayer” (109:4). The curses follow. Romans 12 is written to “brethren,” and in the same chapter the apostle tells them how to answer wrong.",
],
rows=[
("Ps 69:25","Ps 69:25","“Let their habitation be desolate.”"),
("Ps 109:4–8","Ps 109:4–8","“I give myself unto prayer”; “Let his days be few; and let another take his office.”"),
("Ac 1:16–20","Acts 1:16; Acts 1:20","“The Holy Ghost by the mouth of David spake … concerning Judas”; the two verses joined."),
("Mt 5:44","Matt 5:44","The Lord’s word to Israel’s disciples: “Love your enemies.”"),
("Rom 12:14, 19","Rom 12:14; Rom 12:19","To the Body: “bless, and curse not”; “avenge not yourselves.”"),
("2 Tim 4:14","2Tim 4:14","Paul leaves Alexander with “the Lord reward him according to his works.”"),
],
carry=[
("Stated","Peter says the Holy Ghost spoke the psalms “by the mouth of David” and ties them to Judas (Acts 1:16, 20). The psalms are Scripture, and Peter’s use of them stands."),
("Stated","David’s curses in Psalm 109 follow a statement that he prayed for those who hated him for his love (109:4–5). The cursing is spoken as prayer to God, not as an act of the speaker."),
("Shown by the context","Acts 1 is Israel’s company in Jerusalem, and the Sermon on the Mount is spoken to Israel’s disciples (Matthew 5:1). These are in Israel’s line, before Paul’s calling and before the Body."),
("Stated","Romans 12 is written to “brethren” (12:1) and says “bless, and curse not” (12:14) and “avenge not yourselves, but rather give place unto wrath” (12:19). It gives the Body a command that excludes the cursing prayer."),
("Inferred","that the Body does not take up the cursing psalms as its own prayer. No letter to the Body tells it to, and Paul’s letters tell it to bless and to leave wrath to God. Paul’s “let him be accursed” (Galatians 1:8–9) is a judgment on those who preach another gospel and is not a prayer for harm to a personal enemy."),
("Inferred","that the psalms remain true as statements about God’s justice. Paul’s own word about Alexander, “the Lord reward him according to his works” (2 Timothy 4:14), hands the matter to the Lord, which is the heart of the cursing psalms."),
],
other=[
"<b>Believers may pray them as written.</b> Greg Morse (“‘Oh Slay the Wicked’”) allows believers to pray the cursing psalms under severe evil, such as the persecution of the church, notes that the New Testament approves them, and sets Romans 12:19 and Matthew 5:44 beside them. It must explain why Romans 12:14 says “curse not” and why Paul never tells the Body to pray them.",
"<b>An earlier, lower ethic.</b> Some read the cursing psalms as a stage of revelation that Christ replaced. It must explain why Peter says the Holy Ghost spoke them (Acts 1:16) and why the New Testament quotes them as Scripture.",
"<b>Israel’s prayers, applied by Peter to Judas.</b> The reading taken here: they are David’s prayers, Peter applies them to Judas as Israel’s company, and the Body’s word is “bless, and curse not.”",
],
rtbl=[
("Pray them as written","The Body may pray the curses.","“Bless, and curse not”; no command to pray them."),
("A lower ethic, replaced","The cursing was set aside.","“The Holy Ghost by the mouth of David.”"),
("Israel’s prayers","The curses stand in Israel’s line.","None; the Body’s word is Romans 12."),
],
means=[
"The reader may read the cursing psalms as God’s Word and as true about his judgment, and may learn from them that wrong is brought to God and not avenged by hand. The reader is not told to pray them against a person. The Body’s instruction is to bless, to leave wrath to God, and to overcome evil with good.",
],
related="<b>Commentary Series:</b> Acts Commentary, Volume 1 (Acts 1–8). <b>Companions:</b> Acts; Psalms; Romans.",
))
