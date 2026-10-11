"""Study 82 content: The Kinsman-Redeemer."""
META = dict(
    title='The Kinsman-Redeemer',
    subtitle='What the Law Required of a Redeemer, and Where Scripture Says Each Requirement Was Met',
    series='Digital Studies Series', vol=0,
    imprint=('Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. '
             'Licensed for the personal use of the purchaser; no part may be reproduced or distributed without permission. '
             'Scripture quotations are from the King James Version (KJV).'),
)
S1 = '1. The Word and the Law'
S2 = '2. What the Law Requires of a Redeemer'
S3 = '3. The Requirements Applied in Ruth'
S4 = '4. The Redeemer Beyond the Family'
S5 = '5. Hebrews 2:14–17 as Written'
S6 = '6. The Requirements Side by Side'
TOCLIST = ['What You Will Learn in This Study', 'Introduction', S1, S2, S3, S4, S5, S6, 'Conclusion', 'Study Summary',
           'Key Distinctions to Retain', 'Scripture-Tracing Exercise', 'Review and Discussion Questions',
           'Teaching Outline', 'Guided Further Study', 'Final Synthesis']

ALL = []
A = ALL.append

A(('h1', 'What You Will Learn in This Study'))
A(('p', 'By the end of this study, you should be able to:'))
A(('bul', [
    'Follow the Hebrew noun //go’el// through its KJV renderings (“kinsman,” “redeemer,” “revenger of blood”) and note what each passage calls the person who acts.',
    'Read Leviticus 25:23–55 and list who may redeem, what may be redeemed, how the price is set and what the law says happens at the Jubilee.',
    'Walk through Ruth 2:20 to 4:17 in order, marking each step at the threshing floor and the gate: the nearer kinsman, the two matters, the shoe and the witnesses.',
    'Distinguish the law of the near redeemer (Leviticus 25) from the law of the husband’s brother (Deuteronomy 25:5–10) and mark where Ruth’s own words point to each.',
    'Compare Job 19:25, Jeremiah 32:6–15 and Isaiah’s titles for the LORD, recording who is said to act, for whom, and what each passage says is done.',
    'Test Hebrews 2:14–17 against the requirements you have gathered, sorting what the passage states from what it leaves unsaid.',
]))
A(('call', 'Study Goal',
   'To trace the office of the kinsman-redeemer through the passages that state it, from the law in Leviticus to its use of the LORD in Isaiah, and to set down in the text’s own words who may redeem, what the redeemer must be, what is paid and what the redeemed person receives, so that every reading rests on what Scripture says and goes no further.'))
A(('nav', 'Study Outline'))
A(('num', [
    'The Word and the Law: one Hebrew noun, its KJV renderings and Leviticus 25.',
    'What the Law Requires of a Redeemer: nearness, ability, price, willingness and result, with the blood-redeemer of Numbers 35.',
    'The Requirements Applied in Ruth: the threshing floor, the gate, the two matters and the outcome.',
    'The Redeemer Beyond the Family: Job 19, Jeremiah 32, the pleading redeemer and Isaiah’s titles for the LORD.',
    'Hebrews 2:14–17 as Written: what the passage states, and the words it does not use.',
    'The Requirements Side by Side: the comparison, and what this study does not claim.',
    'Conclusion, Study Summary, Key Distinctions, Scripture-Tracing, Review, Teaching Outline, Guided Further Study and Final Synthesis.',
]))

A(('h1', 'Introduction'))
A(('p', 'Few words in the Old Testament carry as much weight as “redeemer,” and few are read as quickly. A reader meets Boaz at the gate in Ruth, or meets “my redeemer liveth” in Job, and the mind moves at once to conclusions the page has not yet stated. This study slows that movement. It begins with what the law required of a near relative who redeemed, reads the one narrative that shows those requirements in operation, and then follows the title to Job, Jeremiah and Isaiah and on to Hebrews 2. At every stop it asks four questions of the text: who may redeem, what must the redeemer be, what is paid, and what does the redeemed person receive?'))
A(('p', 'The study does not retell the whole doctrine of redemption. Study 53 (Redemption) asks what is redeemed, at what price and for which company across Scripture. Study 52 (Sonship and Adoption) asks what legal standing Galatians 4:4–5 describes. This study asks one narrower thing: what did the law require of the person who redeems, and where does Scripture say each requirement was met?'))
A(('p', 'Two habits govern the work. First, each passage is read in its own setting, with its speaker, its audience and its occasion. Second, a link between passages is made only where a passage makes it. When a text leaves a matter unsaid, the study records that and stops.'))

A(('h1', S1))
A(('p', '1.1 One Hebrew noun, several English words. The Hebrew noun //go’el// comes from the verb //ga’al//, “to redeem,” and names the one who redeems. The KJV renders it “kinsman” in Ruth (2:20; 3:9, 12; 4:1, 3, 6, 8, 14), “redeemer” in Job and Isaiah (for example Job 19:25; Isaiah 41:14; 43:14; 44:6, 24; 54:5; 63:16) and “revenger of blood” in Numbers 35:19. An English reader sees three names; a Hebrew reader sees one word used in three settings.'))
A(('call', 'The Word and the Translators’ Choice',
   '“Kinsman,” “redeemer” and “revenger of blood” are the KJV translators’ English choices for one Hebrew noun. This study follows the setting each passage gives. It does not carry a meaning from one setting into another unless the passage itself does.'))
A(('p', '1.2 The setting of the law. The law of redemption sits in Leviticus 25, spoken “in mount Sinai” (25:1) to “the children of Israel” (25:2) concerning the land “which I give you.” It stands inside the law of the sabbatical year and the Jubilee: the land is the LORD’s, and a man’s possession and freedom are guarded by a near relative who may redeem and a fiftieth year that releases.'))
A(('p', '1.3 What the law says. The first table sets out the verses that name the redeemer, the thing redeemed and the way the matter ends. Read it as a list of statements, not yet as a pattern.'))
A(('tbl', '', [
    ('Leviticus 25:23–⁠24', '“The land shall not be sold for ever: for the land is mine; for ye are strangers and sojourners with me. And in all the land of your possession ye shall grant a redemption for the land.”', 'The reason is given first: the land is the LORD’s. Redemption of the land is then commanded as a standing provision.'),
    ('Leviticus 25:25–⁠27', '“If thy brother be waxen poor, and hath sold away some of his possession, and if any of his kin come to redeem it, then shall he redeem that which his brother sold. And if the man have none to redeem it, and himself be able to redeem it; Then let him count the years of the sale thereof, and restore the overplus unto the man to whom he sold it; that he may return unto his possession.”', 'A poor brother has sold land. A kinsman may redeem it. If there is none, the seller himself may redeem it when able, by counting the years and restoring the overplus.'),
    ('Leviticus 25:28', '“But if he be not able to restore it to him, then that which is sold shall remain in the hand of him that hath bought it until the year of jubile: and in the jubile it shall go out, and he shall return unto his possession.”', 'If neither redeems, the land still returns at the Jubilee. The Jubilee is a second provision, not the redeemer’s act.'),
    ('Leviticus 25:48–⁠49', '“After that he is sold he may be redeemed again; one of his brethren may redeem him: Either his uncle, or his uncle’s son, may redeem him, or any that is nigh of kin unto him of his family may redeem him; or if he be able, he may redeem himself.”', 'The thing redeemed is now a person, a poor brother who has sold himself to a stranger (25:47). The text names who may redeem him, outward from a brother to “any that is nigh of kin,” and adds that he may redeem himself if able.'),
    ('Leviticus 25:54–⁠55', '“And if he be not redeemed in these years, then he shall go out in the year of jubile, both he, and his children with him. For unto me the children of Israel are servants; they are my servants whom I brought forth out of the land of Egypt: I am the LORD your God.”', 'The release at the Jubilee is stated again, with its reason in the passage’s own words: the people are the LORD’s servants, brought out of Egypt.'),
], [0.17, 0.44, 0.39]))
A(('p', '1.4 What the chapter redeems. Leviticus 25 names two things that a redeemer may recover: a possession sold by a poor man (25:25–28) and the poor man himself, sold to a stranger (25:47–55). In these verses it speaks of land, of a person’s freedom and of a family’s place in Israel; it says nothing of a debt of sin or of death.'))

A(('h1', S2))
A(('p', '2.1 Nearness. The law does not leave the redeemer undefined. In 25:25 he is “any of his kin”; in 25:48–49 he is “one of his brethren,” then “his uncle, or his uncle’s son,” then “any that is nigh of kin unto him of his family.” The list runs outward from the closest relative, and the word that governs it is nearness. The passage names who is permitted, in the order of nearness; it does not say what happens when the nearest declines.'))
A(('p', '2.2 Ability. Twice the law pairs redemption with ability: the seller who has no redeemer may redeem “himself” when he “be able” (25:26), and the man sold to a stranger may redeem himself “if he be able” (25:49). The text uses the same measure for the poor man and for his kin: a redeemer must be able to pay. Psalm 49:7–9, set beside the law in the next table, states what no brother can do.'))
A(('p', '2.3 The price and its measure. The law does not leave the price to bargaining. The years to the Jubilee are counted (25:27, 50–52), the “overplus” is restored to the buyer, and a man sold to a stranger is reckoned “according to the time of an hired servant” (25:50). The redeemer pays what the remaining years are worth, and no more is required.'))
A(('p', '2.4 The result. When redemption occurs the text states the result in the same words each time: the man “may return unto his possession” (25:27), and the sold brother goes free. When no one redeems, the Jubilee gives the same return without a redeemer (25:28, 54). The redeemer’s act therefore does not create a new right. It brings an existing right forward, within the years remaining.'))
A(('p', '2.5 Willingness. Leviticus 25:25 says that the kinsman “shall” redeem that which his brother sold, and 25:48–49 say that a brother or relative “may,” but these verses state no penalty for a kinsman who does not. Where the law does take up refusal, it does so in a different statute, the law of the brother who will not raise up a name for his dead brother (Deuteronomy 25:7–10), which Section 3 sets beside Ruth. Willingness therefore becomes visible in the narrative, not in the statute of redemption.'))
A(('p', '2.6 The same noun in a different setting. Numbers 35 uses //go’el// of the near relative of a slain man, whom the KJV calls “the avenger” (35:12) and “the revenger of blood” (35:19).'))
A(('tbl', 'The second table sets the blood-redeemer and Psalm 49 beside the law of Leviticus 25, so that the same noun and the limits on any brother’s power can be seen at once.', [
    ('Numbers 35:12', '“And they shall be unto you cities for refuge from the avenger; that the manslayer die not, until he stand before the congregation in judgment.”', 'The avenger is named, and the manslayer is protected until a congregation judges. The near relative’s act is bounded by process.'),
    ('Numbers 35:19', '“The revenger of blood himself shall slay the murderer: when he meeteth him, he shall slay him.”', 'The same Hebrew noun as “kinsman” in Ruth. Here the near relative acts for a slain kinsman, and the text says no more of his office than this.'),
    ('Numbers 35:24–⁠25', '“Then the congregation shall judge between the slayer and the revenger of blood according to these judgments: And the congregation shall deliver the slayer out of the hand of the revenger of blood …”', 'The congregation judges between the two. The law places the near relative inside a public process.'),
    ('Psalm 49:7–⁠9', '“None of them can by any means redeem his brother, nor give to God a ransom for him: (For the redemption of their soul is precious, and it ceaseth for ever:) That he should still live for ever, and not see corruption.”', 'A psalm states what no brother can do: redeem a brother, or give God a ransom. It speaks of the soul and of corruption, not of sold land or a sold man.'),
], [0.17, 0.44, 0.39]))
A(('p', '2.7 Reading the two statements together. Leviticus 25 says that a brother may redeem a brother from a sale into poverty; Psalm 49 says that no brother can redeem a brother from the corruption of death. The passages name different things to be redeemed, a possession and a person’s freedom in one, the life itself in the other, and a reader who removes that difference makes one of them say what it does not say.'))

A(('h1', S3))
A(('p', '3.1 The setting. The book opens “in the days when the judges ruled” (Ruth 1:1), with a famine and a family that goes to Moab. By chapter 2 two widows are in Bethlehem, and the question Leviticus 25 raises becomes a question about particular people: is there a near relative who may redeem?'))
A(('p', '3.2 The kinsman is named. The narrator introduces Boaz as “a kinsman of her husband’s, a mighty man of wealth, of the family of Elimelech” (2:1). When Ruth reports his kindness, Naomi answers with the word of the law: “The man is near of kin unto us, one of our next kinsmen” (2:20). The first step toward redemption is a recognition: the one who has shown kindness is within the circle the law names.'))
A(('p', '3.3 The threshing floor. In chapter 3 Ruth asks Boaz to “spread therefore thy skirt over thine handmaid; for thou art a near kinsman” (3:9). Boaz answers with the two statements the third table sets side by side: he is a near kinsman, and there is a nearer one.'))
A(('tbl', 'The third table follows the kinsman through the book in order, so that each requirement of Section 2 can be looked for in the narrative.', [
    ('Ruth 2:20', '“And Naomi said unto her daughter in law, Blessed be he of the LORD, who hath not left off his kindness to the living and to the dead. And Naomi said unto her, The man is near of kin unto us, one of our next kinsmen.”', 'Nearness is stated first, by Naomi, in the law’s own term.'),
    ('Ruth 3:12–⁠13', '“And now it is true that I am thy near kinsman: howbeit there is a kinsman nearer than I. Tarry this night, and it shall be in the morning, that if he will perform unto thee the part of a kinsman, well; let him do the kinsman’s part: but if he will not do the part of a kinsman to thee, then will I do the part of a kinsman to thee, as the LORD liveth: lie down until the morning.”', 'Boaz states an order (a nearer kinsman first) and puts willingness in conditional form: “if he will,” “if he will not.”'),
    ('Ruth 4:5–⁠6', '“Then said Boaz, What day thou buyest the field of the hand of Naomi, thou must buy it also of Ruth the Moabitess, the wife of the dead, to raise up the name of the dead upon his inheritance. And the kinsman said, I cannot redeem it for myself, lest I mar mine own inheritance: redeem thou my right to thyself; for I cannot redeem it.”', 'Boaz has offered the field and the nearer kinsman has said he will redeem it (4:4); he declines when the second matter is named. The text gives his reason: “lest I mar mine own inheritance.”'),
    ('Ruth 4:9–⁠10', '“And Boaz said unto the elders, and unto all the people, Ye are witnesses this day, that I have bought all that was Elimelech’s, and all that was Chilion’s and Mahlon’s, of the hand of Naomi. Moreover Ruth the Moabitess, the wife of Mahlon, have I purchased to be my wife, to raise up the name of the dead upon his inheritance, that the name of the dead be not cut off from among his brethren, and from the gate of his place: ye are witnesses this day.”', 'The purchase is stated as done, before witnesses at the gate. It names two things bought: the inheritance and Ruth, and gives one purpose for the second: the dead man’s name.'),
    ('Ruth 4:14–⁠15', '“And the women said unto Naomi, Blessed be the LORD, which hath not left thee this day without a kinsman, that his name may be famous in Israel. And he shall be unto thee a restorer of thy life, and a nourisher of thine old age: …”', 'The women bless the LORD for a kinsman and speak of a “restorer of thy life.” The verses report what was said at the child’s birth; they do not say more than that.'),
], [0.17, 0.44, 0.39]))
A(('p', '3.4 Two matters at the gate. The gate scene turns on two things. The first is the field of Elimelech, which Naomi is selling (4:3). The second is Ruth, “to raise up the name of the dead upon his inheritance” (4:5). The nearer kinsman agrees to the first and declines when the second is joined to it, and the text states why: he fears to “mar mine own inheritance” (4:6). The study records the reason without grading it; the passage names his cost and does not call him wicked. His answer is the nearest the book comes to the law’s measure of ability: “I cannot redeem it.”'))
A(('p', '3.5 The shoe and the witnesses. The narrator pauses to explain the custom: “Now this was the manner in former time in Israel concerning redeeming and concerning changing, for to confirm all things; a man plucked off his shoe, and gave it to his neighbour: and this was a testimony in Israel” (4:7). The nearer kinsman gives Boaz his shoe with the words “Buy it for thee” (4:8), and ten elders and all the people are witnesses (4:2, 9–11). The transfer is public, spoken and attested.'))
A(('p', '3.6 A different shoe in Deuteronomy. A shoe is also named in Deuteronomy 25:5–10, and the two passages are easy to run together. There the law concerns “brethren” who “dwell together”; one dies childless, and “her husband’s brother” is to “take her to him to wife” so that “the firstborn which she beareth shall succeed in the name of his brother which is dead, that his name be not put out of Israel” (25:5–6). If the brother refuses, the widow brings the matter “to the gate unto the elders,” and she looses his shoe and spits in his face (25:7–9). In Ruth the kinsman takes off his own shoe as a sign of transfer, and there is no spitting.'))
A(('call', 'Two Laws in Ruth, Not One',
   'Ruth’s own words point to two provisions. The land is spoken of with the vocabulary of Leviticus 25: “redeem,” “buy,” “inheritance.” The widow is spoken of with the vocabulary of Deuteronomy 25: “raise up the name of the dead upon his inheritance” (4:5, 10), compare “raise up unto his brother a name in Israel” (Deuteronomy 25:7). The book never says that the two laws are one law, and it does not use the words “her husband’s brother” of Boaz. It reports a transaction in which both provisions are in view.'))
A(('p', '3.7 The outcome as the text reports it. Boaz takes Ruth, “the LORD gave her conception,” and she bears a son (4:13). The women say that the LORD “hath not left thee this day without a kinsman” (4:14), call the child “a restorer of thy life” (4:15) and name him Obed, “the father of Jesse, the father of David” (4:17). The text does not say which person the “kinsman” of 4:14 is; the verse and the next carry on to the child’s name and role, and the study leaves the reference as written.'))
A(('p', '3.8 What the narrative states. Ruth shows nearness (2:20; 3:12), an order of nearness (3:12; 4:4), ability and willingness in the kinsman’s own words (3:13; 4:4–6), a price paid before witnesses (4:9–10) and a result: a field redeemed, a name raised up and a household restored.'))
A(('call', 'What the Text Does Not Say About Boaz',
   'Ruth does not call Boaz a picture, a type or a figure of anyone, and it does not describe the redemption of the field and the household as the redemption of a soul. The passage is silent on both matters, and this study does not supply what it leaves unsaid.'))

A(('h1', S4))
A(('p', '4.1 Job 19:25–27. In the middle of his complaint Job says, “For I know that my redeemer liveth, and that he shall stand at the latter day upon the earth: And though after my skin worms destroy this body, yet in my flesh shall I see God: Whom I shall see for myself, and mine eyes shall behold, and not another; though my reins be consumed within me.” The verses are reported as written: Job says that he knows, that his redeemer lives and that he himself shall see God. The passage does not say who the redeemer is, what he pays or when the “latter day” falls, and the study reasons no further than the words reach.'))
A(('p', '4.2 Jeremiah 32:6–15. Here the law of the near redeemer appears in a prophet’s own life. The setting is stated plainly: Jerusalem is under siege in the tenth year of Zedekiah, and Jeremiah is “shut up in the court of the prison” (32:1–2). The LORD tells him that his uncle’s son will offer him a field in Anathoth: “for the right of redemption is thine to buy it” (32:7). Hanameel comes and says the same: “the right of inheritance is thine, and the redemption is thine; buy it for thyself” (32:8). Jeremiah buys, weighs the seventeen shekels of silver, signs and seals “the evidence of the purchase, both that which was sealed according to the law and custom, and that which was open,” and takes witnesses (32:9–12).'))
A(('p', '4.3 What the transaction states. Four of the law’s requirements appear in the text. The redeemer is a near relative (an uncle’s son, as in Leviticus 25:49). He has the right of redemption by that nearness. He pays a stated price in the presence of witnesses. And the LORD gives the meaning of the purchase: “Houses and fields and vineyards shall be possessed again in this land” (32:15). The purchase is made while the land is about to be taken, under the promise that it will be possessed again.'))
A(('p', '4.4 The redeemer who pleads. Two passages speak of a redeemer who does something the law of Leviticus 25 does not mention: “For their redeemer is mighty; he shall plead their cause with thee” (Proverbs 23:11), and “Their Redeemer is strong; the LORD of hosts is his name: he shall throughly plead their cause, that he may give rest to the land” (Jeremiah 50:34). The redeemer here defends the weak before an adversary. Proverbs sets the redeemer beside the warning “Remove not the old landmark,” and in Jeremiah the redeemer is the LORD and the adversary is Babylon.'))
A(('p', '4.5 The LORD as Redeemer in Isaiah. The title becomes a name of the LORD in Isaiah, where it is addressed to Jacob and Israel. The fourth table lists the passages for study, with the addressee and the relation named in each.'))
A(('tbl', '', [
    ('Isaiah 41:14', '“Fear not, thou worm Jacob, and ye men of Israel; I will help thee, saith the LORD, and thy redeemer, the Holy One of Israel.”', 'The title is given to Jacob and Israel in a word of comfort. “Redeemer” stands beside “the Holy One of Israel.”'),
    ('Isaiah 43:14', '“Thus saith the LORD, your redeemer, the Holy One of Israel; For your sake I have sent to Babylon, and have brought down all their nobles …”', 'The Redeemer acts against Babylon “for your sake.” The act is named.'),
    ('Isaiah 44:22, 24', '“I have blotted out, as a thick cloud, thy transgressions, and, as a cloud, thy sins: return unto me; for I have redeemed thee. … Thus saith the LORD, thy redeemer, and he that formed thee from the womb …”', 'Redemption is spoken of as already done, joined to blotting out of transgressions and to an appeal, “return unto me.” The Redeemer is also the one who formed Israel “from the womb.”'),
    ('Isaiah 54:5', '“For thy Maker is thine husband; the LORD of hosts is his name; and thy Redeemer the Holy One of Israel; The God of the whole earth shall he be called.”', 'Three relations stand in one verse: Maker, husband and Redeemer. The text sets them side by side and does not rank them.'),
    ('Isaiah 63:16', '“Doubtless thou art our father, though Abraham be ignorant of us, and Israel acknowledge us not: thou, O LORD, art our father, our redeemer; thy name is from everlasting.”', 'Here the people speak to the LORD. They name him “father” and “redeemer” and set him against Abraham and Israel as ancestors.'),
], [0.17, 0.44, 0.39]))
A(('p', '4.6 What the Isaiah passages state. In each, the Redeemer is the LORD, the one redeemed is Jacob or Israel, and the title stands with relations of nearness: Maker, husband, father. The passages do not use the word “kinsman” or describe a price in coin; they state the LORD’s acts (help, judgment of Babylon, blotting out of sins) and the nearness of his relation. Isaiah 59:20 (“And the Redeemer shall come to Zion”) uses the same title and is treated with its setting in Study 53; it is noted here only as the same word.'))
A(('p', '4.7 Gathering the Old Testament evidence. A near relative who redeems, a prophet’s purchase, a Redeemer who pleads and a title of the LORD in Isaiah are different uses of one noun. The study does not claim that any one of them explains the others.'))

A(('h1', S5))
A(('p', '5.1 The audience and the setting. Hebrews 2:1–3 supplies the passage’s own markers: “we ought to give the more earnest heed to the things which we have heard,” and the great salvation “at the first began to be spoken by the Lord, and was confirmed unto us by them that heard him.” The speaker includes himself with the hearers. This reading rests on the letter’s own audience markers and setting.'))
A(('p', '5.2 The words the passage does not use. Hebrews 2 contains none of the words “kinsman,” “redeemer,” “redeem,” “redemption,” “ransom,” “price” or “bought.” The passage speaks instead of children, flesh and blood, death, bondage, brethren, the seed of Abraham, a high priest and reconciliation. To find the kinsman-redeemer here is to lay the requirements of Leviticus and Ruth beside the passage and test the facts it states; the passage supplies no such word.'))
A(('tbl', 'The fifth table gives the passage in order, with the facts each verse states.', [
    ('Hebrews 2:14–⁠15', '“Forasmuch then as the children are partakers of flesh and blood, he also himself likewise took part of the same; that through death he might destroy him that had the power of death, that is, the devil; And deliver them who through fear of death were all their lifetime subject to bondage.”', 'The children share flesh and blood, and “he also himself likewise took part of the same.” The purpose clauses are “destroy” the one with the power of death and “deliver” those in bondage.'),
    ('Hebrews 2:16', '“For verily he took not on him the nature of angels; but he took on him the seed of Abraham.”', 'The passage states whom he “took on him”: the seed of Abraham, not angels.'),
    ('Hebrews 2:17', '“Wherefore in all things it behoved him to be made like unto his brethren, that he might be a merciful and faithful high priest in things pertaining to God, to make reconciliation for the sins of the people.”', 'He is “made like unto his brethren” in all things. The stated purpose is that he be a high priest, to make reconciliation “for the sins of the people.”'),
    ('Hebrews 2:18', '“For in that he himself hath suffered being tempted, he is able to succour them that are tempted.”', 'The passage uses the word “able” of what he does for the tempted. It says that he is able to succour.'),
], [0.17, 0.44, 0.39]))
A(('p', '5.3 The matches the text states. Nearness: the children share flesh and blood and he “took part of the same” (2:14), and he is “made like unto his brethren” (2:17). Death and deliverance: “through death” he acts, and those in “bondage” are delivered (2:14–15). A statement of ability: he “is able to succour” the tempted (2:18). A stated purpose: “reconciliation for the sins of the people” (2:17).'))
A(('call', 'Hebrews as Written',
   'Hebrews 2:14–17 names flesh and blood shared, brethren, the seed of Abraham, death, deliverance from bondage and a high priest. It does not use “kinsman,” “redeemer,” “redeem,” “ransom” or “price,” and the study adds no word the passage lacks.'))
A(('p', '5.4 The matches the passage does not state. Hebrews 2 does not speak of a price in the vocabulary of Leviticus 25, does not name a field or a name to be raised, and does not use the word “kinsman.” It does not say how the “children” and “brethren” of 2:11–14 relate to any other company beyond what the passage says, and the study does not decide that; the letter addresses its own hearers (2:1–4) and quotes the Scriptures of Israel to them.'))

A(('h1', S6))
A(('p', '6.1 The two comparison tables. The first sets the requirements from Section 2 beside the law and Ruth; the second sets them beside the passages that apply the title to the LORD and beside Hebrews 2. Where a text does not speak to a requirement, the cell says so, because the absence is itself a finding.'))
A(('ctbl', '', [
    ['Requirement', 'In the law (Leviticus 25; Numbers 35)', 'In Ruth'],
    ['Nearness', '“any of his kin,” “one of his brethren,” “his uncle, or his uncle’s son,” “any that is nigh of kin” (Leviticus 25:25, 48–49)', '“near of kin … one of our next kinsmen” (2:20); “near kinsman … a kinsman nearer than I” (3:9, 12)'],
    ['Order', 'A list outward from the closest relative (Leviticus 25:48–49)', '“a kinsman nearer than I” (3:12); “I am after thee” (4:4)'],
    ['Ability', '“himself be able to redeem it” (25:26); “if he be able” (25:49)', '“I cannot redeem it” (4:6), with the reason given'],
    ['Willingness', 'Not stated in the statute of redemption; refusal handled in Deuteronomy 25:7–10', '“if he will … if he will not” (3:13); “I will redeem it” then “I cannot” (4:4–6)'],
    ['Price', 'Counted by the years to the Jubilee (25:27, 50–52)', '“bought … purchased” before ten elders and the people (4:9–10)'],
    ['Result', 'Return to possession, freedom (25:27, 54)', 'The inheritance bought, a name raised up, a son born (4:9–13)'],
], [0.19, 0.42, 0.39]))
A(('p', '6.2 The second table.'))
A(('ctbl', '', [
    ['Requirement', 'The title applied to the LORD (Job, Jeremiah, Proverbs, Isaiah)', 'Hebrews 2:14–18'],
    ['Nearness', 'Relations stated: Maker, husband, father (Isaiah 54:5; 63:16)', '“partakers of flesh and blood … took part of the same”; “made like unto his brethren” (2:14, 17)'],
    ['Ability', '“mighty,” “strong” (Proverbs 23:11; Jeremiah 50:34)', '“is able to succour” (2:18)'],
    ['Price', 'No price in coin is named in the Isaiah passages', 'No price named; “through death” (2:14)'],
    ['Willingness', 'Not stated as such', 'Not stated as such; “it behoved him” (2:17)'],
    ['Result', 'Help, judgment of Babylon, sins blotted out (Isaiah 41:14; 43:14; 44:22); rest for the land (Jeremiah 50:34)', 'Death destroyed in its power; deliverance from bondage; reconciliation for the sins of the people (2:14–15, 17)'],
], [0.19, 0.42, 0.39]))
A(('p', '6.3 What the study does not claim. Beyond the limits stated for Boaz and Ruth, three more apply.'))
A(('bul', [
    'Job 19:25 is not assigned a meaning beyond its words: no passage in this study says who Job’s redeemer is.',
    'Hebrews 2:14–17 is read as a statement to its own hearers; its “children” and “brethren” are not identified with any company the passage does not name.',
    'Redemption across Scripture, including the redemption of the Body of Christ in its own passages, is the subject of Study 53 and is not decided here.',
]))

A(('h1', 'Conclusion'))
A(('p', 'The law required of a redeemer that he be near, that he be able, that he pay a price measured by the Jubilee, and that the result be a return to possession or freedom. Ruth shows these spoken by the persons concerned and carried out before witnesses; Jeremiah shows the same law carried out by a prophet. Job, Proverbs, Jeremiah 50 and Isaiah apply the title to a redeemer who lives, who is mighty and who is the LORD himself. Hebrews 2 states facts of nearness, death, deliverance, ability and reconciliation without using the words of the law.'))

A(('h1', 'Study Summary'))
A(('bul', [
    'The Hebrew //go’el// names the one who redeems, and the KJV renders it “kinsman,” “redeemer” and “revenger of blood.”',
    'Leviticus 25 names what may be redeemed (land, a person), who may redeem (a near relative, then the poor man himself if able), how the price is measured (the years to the Jubilee) and the result (return and freedom).',
    'Ruth applies the requirements in a narrative: a near kinsman, a nearer kinsman, two matters at the gate, a price before witnesses and a household restored.',
    'Job, Jeremiah, Proverbs and Isaiah show the title in other uses: a living redeemer, a prophet’s purchase, a redeemer who pleads and the LORD as Redeemer of Israel.',
    'Hebrews 2:14–17 states facts that can be set beside the requirements and uses none of the words of the law.',
]))

A(('h1', 'Key Distinctions to Retain'))
A(('bul', [
    'One Hebrew noun, three English words: the setting governs the meaning, not the translator’s word.',
    'The law of the near redeemer (Leviticus 25) and the law of the husband’s brother (Deuteronomy 25:5–10) are two laws, both in view in Ruth.',
    'A brother can redeem a brother’s possession or freedom (Leviticus 25), but no brother can redeem him from death (Psalm 49:7–9).',
]))

A(('h1', 'Scripture-Tracing Exercise'))
A(('p', 'Trace the argument in the order below. For each step, read the passage in its chapter, write what the text states in one sentence, and mark what it does not say.'))
A(('num', [
    'Read Leviticus 25:23–28 and list the person, the thing redeemed, the redeemer and the result.',
    'Read Leviticus 25:47–55 and add the second thing redeemed and the reason stated in verse 55.',
    'Read Numbers 35:12, 19, 24–25 and note the same noun in a different office.',
    'Read Ruth 2:1, 2:20 and 3:9–13, and list nearness, order and willingness as the persons state them.',
    'Read Ruth 4:1–10 and mark the two matters, the refusal and the witnesses.',
    'Read Deuteronomy 25:5–10 and write two differences from Ruth 4:7–8.',
    'Read Job 19:23–27 and Jeremiah 32:6–15 and write what each says is done, and by whom.',
    'Read Isaiah 43:14, 44:22–24, 54:5 and 63:16 and record the relation named in each.',
    'Read Hebrews 2:1–18 and record the words used and the words absent.',
]))

A(('h1', 'Review and Discussion Questions'))
A(('num', [
    'Which three English words does the KJV use for the Hebrew //go’el//, and what two things does Leviticus 25 say a redeemer may recover?',
    'What two matters are before the elders at the gate in Ruth 4, and what reason does the nearer kinsman give?',
    'How does the shoe in Ruth 4:7–8 differ from the shoe in Deuteronomy 25:9?',
    'What does Psalm 49:7–9 say no brother can do, and how does that differ from Leviticus 25?',
    'What does Hebrews 2:14–17 state, and which words of Leviticus and Ruth does it not use?',
]))

A(('h1', 'Teaching Outline'))
A(('p', 'I. The word. A. One Hebrew noun. B. Three English words. C. The setting governs.'))
A(('p', 'II. The law. A. Land and person (Leviticus 25). B. Nearness, ability, price, result. C. Numbers 35 and Psalm 49.'))
A(('p', 'III. The narrative. A. The threshing floor. B. The gate and the two matters. C. The outcome.'))
A(('p', 'IV. The title elsewhere. A. Job and Jeremiah. B. The redeemer who pleads. C. Isaiah’s titles.'))
A(('p', 'V. The comparison. A. Hebrews 2 as written. B. The tables. C. The limits.'))

A(('h1', 'Guided Further Study'))
A(('p', 'For each group, read the passages in context, observe the assigned point, compare it with the requirements in this study, and write one sentence of conclusion.'))
A(('p', 'Group 1: Other redemptions in the law. Read Leviticus 27:13 (“But if he will at all redeem it, then he shall add a fifth part thereof unto thy estimation”) and Exodus 13:13. Observe what is redeemed and what is added. Compare with Leviticus 25. Conclude whether the near-relative requirement appears in these passages.'))
A(('p', 'Group 2: The line of Judah. Read Genesis 38:8 (“Go in unto thy brother’s wife, and marry her, and raise up seed to thy brother”) and Ruth 4:12. Observe the language of raising up, compare it with Deuteronomy 25:5–10 and conclude how Ruth’s words relate to each.'))
A(('p', 'Group 3: The pleading redeemer. Read Proverbs 23:10–11, Jeremiah 50:34 and Psalm 107:2. Observe who is defended and from whom. Compare with Leviticus 25 and conclude what the pleading redeemer adds.'))
A(('p', 'Group 4: The context of Hebrews 2. Read Hebrews 2:1–13. Observe the audience markers and the quotations, compare with the requirements and conclude which facts the passage states.'))

A(('h1', 'Final Synthesis'))
A(('p', 'In about 250 words, state the requirements of a redeemer as the law gives them, show where Ruth reports each, show how Job, Jeremiah and Isaiah apply the title and record what Hebrews 2:14–17 states, quoting each passage. Close with what the study did not claim.'))
