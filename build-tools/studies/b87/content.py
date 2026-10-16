"""Study 87 content: The Last Days (every place the KJV prints "the last days", "the latter days" and near wordings)."""
META = dict(
    title='The Last Days',
    subtitle='Where Scripture Uses the Phrase, of Whom Each Passage Speaks, and What It Leaves Unsaid',
    series='Digital Studies Series', vol=0,
    imprint=('Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. '
             'Licensed for the personal use of the purchaser; no part may be reproduced or distributed without permission. '
             'Scripture quotations are from the King James Version (KJV).'),
)
S1 = '1. The Phrase and Its Neighbours'
S2 = '2. Jacob, Balaam and Moses'
S3 = '3. The Prophets: Isaiah, Micah, Jeremiah, Ezekiel, Hosea and Daniel'
S4 = '4. Other Time Words: Daniel, “Latter End” and “The Last Day”'
S5 = '5. Acts 2:14–21: Peter and the Words of Joel'
S6 = '6. Letters to Scattered Readers'
S7 = '7. Letters to Timothy and One Word to Corinth'
S8 = '8. The Passages Side by Side and Three Readings Tested'
TOCLIST = ['What You Will Learn in This Study', 'Introduction', S1, S2, S3, S4, S5, S6, S7, S8, 'Conclusion',
           'Study Summary', 'Key Distinctions to Retain', 'Scripture-Tracing Exercise',
           'Review and Discussion Questions', 'Teaching Outline', 'Guided Further Study', 'Final Synthesis']

ALL = []
A = ALL.append

A(('h1', 'What You Will Learn in This Study'))
A(('p', 'By the end of this study, you should be able to:'))
A(('bul', [
    'Locate each place where the King James Version prints “the last days,” “the latter days” or a near wording, and sort them by the exact words used.',
    'Read each passage in its own chapter and mark who speaks, who is addressed and what the passage says follows the phrase.',
    'Compare Isaiah 2:2 with Micah 4:1, and Joel’s opening words with Peter’s, and record which words agree and which differ.',
    'Follow the tense of the verbs in the New Testament passages (“hath spoken,” “was manifest,” “is,” “shall come,” “should be”) without reconciling them beyond the text.',
    'Trace how the writers of the letters introduce the phrase, and note which readers each letter names for itself.',
    'Test three common readings of the phrase against its own wording, sorting what the text states from what readers add.',
]))
A(('call', 'Study Goal',
   'To read every place where the King James Version prints “the last days,” “the latter days” and their near wordings, in the order of the canon and in their own chapters, and to set down who speaks, who hears, what each passage says follows and what it leaves unsaid, so that every reading of the phrase rests on no more than the words state.'))
A(('nav', 'Study Outline'))
A(('num', [
    'The Phrase and Its Neighbours: the wordings the King James Version prints, and the questions put to each.',
    'Jacob, Balaam and Moses: Genesis 49:1; Numbers 24:14; Deuteronomy 4:30 and 31:29.',
    'The Prophets: Isaiah 2:2 and Micah 4:1; Jeremiah; Ezekiel 38; Hosea 3:5; Daniel 2:28 and 10:14.',
    'Other Time Words: Daniel’s “time of the end,” “latter end” and “the last day.”',
    'Acts 2:14–21: Peter and the Words of Joel.',
    'Letters to Scattered Readers: Hebrews, James, 1 Peter, 2 Peter, 1 John and Jude.',
    'Letters to Timothy and One Word to Corinth: 1 Timothy 4:1; 2 Timothy 3:1; 1 Corinthians 10:11.',
    'The Passages Side by Side and Three Readings Tested: two tables and three readings set against the words.',
    'Conclusion, Study Summary, Key Distinctions, Scripture-Tracing, Review, Teaching Outline, Guided Further Study and Final Synthesis.',
]))

A(('h1', 'Introduction'))
A(('p', '“The last days” and “the latter days” are phrases heard in sermons, charts and headlines, and they are usually taken to name one period. The King James Version prints “the last days” eight times and “the latter days” eleven, and it prints near wordings (“the latter years,” “the latter times,” “the last time,” “the time of the end,” “the end of the days”) in other places. The words are spoken by Jacob, Balaam, Moses, Isaiah, Micah, Jeremiah, Ezekiel, Daniel, Hosea, Peter, Paul, James, John and Jude and by the writer to the Hebrews, to different hearers in different settings. A phrase that is shared among so many speakers invites a single answer, and the question this study asks is whether the passages themselves give one.'))
A(('p', 'This study reads each place in its own chapter. It does not take up Study 7 (The Day of the Lord), which reads the passages on that day across the Scriptures; Study 20 (Understanding Acts 2:38) sets Joel 2:28–32 beside Acts 2:16–21 for the sake of Acts 2:38, while this study reports only the opening phrase of Acts 2:17; Study 74 (The Man of Sin) reports the final-ruler passages, and this study reads 1 John 2:18 only for the words “the last time”; and Study 80 (The Lamb Foreordained) reads 1 Peter 1:20 among the passages on the foundation of the world, while this study reads it only for “these last times.” This study asks one narrower question: where does the King James Version print “the last days,” “the latter days” and their near wordings, to whom is each spoken, what does each passage say follows, and what does each leave unsaid?'))
A(('p', 'Two habits govern the work. First, each passage is read in its own place, with its speaker, its audience and the sentence that carries the phrase. Second, a link between passages is made only where a passage makes it. A shared phrase is not treated as a shared period unless a passage says so. This reading rests on the passages’ own audience markers and setting. Where the text is silent, the study records the silence and stops.'))

A(('h1', S1))
A(('p', '1.1 What the King James Version prints. The table lists the wordings by their English form. The study reads the English as printed and does not argue from the original words; where a passage needs more than its English wording, the passage is left to say it.'))
A(('ctbl', '', [
    ['Wording', 'Where it stands', 'Count'],
    ['“the last days”', 'Gen 49:1; Isa 2:2; Mic 4:1; Acts 2:17; 2 Tim 3:1; Heb 1:2; Jas 5:3; 2 Pet 3:3', 'Eight verses'],
    ['“the latter days”', 'Num 24:14; Deut 4:30; 31:29; Jer 23:20; 30:24; 48:47; 49:39; Ezek 38:16; Dan 2:28; 10:14; Hos 3:5', 'Eleven verses'],
    ['“the latter years”; “the latter times”; “the latter time”', 'Ezek 38:8; 1 Tim 4:1; Dan 8:23', 'One verse each'],
    ['“the last time”; “these last times”', '1 Pet 1:5; 1 Pet 1:20; 1 John 2:18; Jude 18', 'Four verses'],
    ['“the time of the end”; “the end of the days”', 'Dan 8:17; 11:35, 40; 12:4, 9; Dan 12:13', 'Six verses'],
    ['“the last day”; “the latter day”', 'John 6:39, 40, 44, 54; 7:37; 11:24; 12:48; Job 19:25', 'Eight verses'],
], [0.3, 0.52, 0.18]))
A(('p', '1.2 The questions put to each place. For every passage the study asks four things: who speaks, who is addressed, what the passage says follows the phrase, and what the passage does not say. The answers are recorded in the words of the passage. The study does not give a date to any of them and does not say that one place names the same time as another.'))
A(('call', 'How the Study Reads the Phrase',
   'Each place is read for four things: who speaks, who is addressed, what the passage says follows and what it leaves unsaid. A shared phrase is not a shared period unless a passage makes it so.'))
A(('p', '1.3 What the study will not do. It will not date any passage or add a length of time to a phrase that gives none. It will not take a meaning from one passage and carry it into another unless the passage itself does so. Where the New Testament uses wording found in the Old Testament, the study records the wording and the setting and adds no conclusion about how much of the earlier passage is in view.'))

A(('h1', S2))
A(('p', '2.1 The four passages. The first uses of the phrase stand in the Law. Jacob speaks to his sons, Balaam to Balak, and Moses twice to Israel. The table sets the wording beside the setting.'))
A(('tbl', '', [
    ('Gen 49:1–2', '“Gather yourselves together, that I may tell you that which shall befall you in the last days.” “Gather yourselves together, and hear, ye sons of Jacob; and hearken unto Israel your father.”', 'Jacob speaks to his sons. The phrase is “the last days.” The chapter that follows speaks son by son (49:3–27).'),
    ('Num 24:14', '“And now, behold, I go unto my people: come therefore, and I will advertise thee what this people shall do to thy people in the latter days.”', 'Balaam speaks to Balak. “This people” is said to do something “to thy people.” The phrase is “the latter days.”'),
    ('Deut 4:30–31', '“When thou art in tribulation, and all these things are come upon thee, even in the latter days, if thou turn to the LORD thy God, and shalt be obedient unto his voice;” “he will not forsake thee, neither destroy thee, nor forget the covenant of thy fathers which he sware unto them.”', 'Moses speaks to Israel after naming scattering (4:27) and idols (4:28). The sentence carries a condition (“if thou turn”) and a statement of what the LORD will not do.'),
    ('Deut 31:29', '“For I know that after my death ye will utterly corrupt yourselves, and turn aside from the way which I have commanded you; and evil will befall you in the latter days;”', 'Moses speaks to the elders and officers (31:28). The sentence names a corruption “after my death” and “evil” that “will befall” them.'),
], [0.15, 0.5, 0.35]))
A(('p', '2.2 What the passages state. In Genesis 49:1 the phrase is attached to what “shall befall” Jacob’s sons. In Numbers 24:14 it is attached to what “this people shall do to thy people.” In Deuteronomy 4:30 it stands in a sentence that begins with tribulation and ends with a call to turn and obey, and verse 31 adds a statement about the covenant of the fathers. In Deuteronomy 31:29 it stands in a sentence about corruption and evil. In each case the speaker is a man speaking to hearers he names or addresses in the setting.'))
A(('p', '2.3 The words that are not “the latter days.” Numbers 24:20 uses a different word: “his latter end shall be that he perish for ever.” The sentence is about Amalek, and “latter end” is not “latter days.” Deuteronomy 8:16 uses “latter end” of Israel in the wilderness: “to do thee good at thy latter end.” The study keeps the two kinds of sentence apart.'))
A(('p', '2.4 What the passages leave unsaid. No verse in this group gives a date or a length. None says that the days of Genesis 49:1 and the days of Numbers 24:14 are the same days. None says that the “latter days” of Deuteronomy 4:30 and 31:29 are one period, though the same words stand in both. Deuteronomy 4:30 does not say how the condition “if thou turn” is met, and 31:29 does not say how the evil relates to the tribulation of 4:30.'))
A(('call', 'What Deuteronomy 4:30 and 31:29 State',
   'Both verses say “the latter days,” and both are spoken by Moses to Israel. In 4:30 the sentence carries tribulation, a condition and a promise about the covenant; in 31:29 it carries corruption and evil. The text does not join them or date either.'))

A(('h1', S3))
A(('p', '3.1 Isaiah 2:2 beside Micah 4:1. The two prophets give almost the same words about “the last days.” The table sets them side by side. Isaiah’s passage is introduced as “the word that Isaiah the son of Amoz saw concerning Judah and Jerusalem” (2:1).'))
A(('ctbl', '', [
    ['Isaiah 2', 'Micah 4', 'Observation'],
    ['“And it shall come to pass in the last days, that the mountain of the LORD’s house shall be established in the top of the mountains” (2:2)', '“But in the last days it shall come to pass, that the mountain of the house of the LORD shall be established in the top of the mountains” (4:1)', 'The phrase and the main sentence agree; the order of the opening words differs.'],
    ['“all nations shall flow unto it” (2:2)', '“people shall flow unto it” (4:1)', 'Isaiah says “all nations”; Micah says “people.”'],
    ['“out of Zion shall go forth the law, and the word of the LORD from Jerusalem” (2:3)', '“the law shall go forth of Zion, and the word of the LORD from Jerusalem” (4:2)', 'The sentence is recast with the same two places.'],
    ['“nation shall not lift up sword against nation, neither shall they learn war any more” (2:4)', '“nation shall not lift up a sword against nation, neither shall they learn war any more” (4:3)', 'The sentence agrees apart from one word.'],
], [0.37, 0.37, 0.26]))
A(('p', '3.2 The others. The table gives the remaining prophetic uses in the order of the books. Each is read in its own sentence and with the people named in it.'))
A(('tbl', '', [
    ('Jer 23:19–20; 30:23–24', '“The anger of the LORD shall not return, until he have executed, and till he have performed the thoughts of his heart: in the latter days ye shall consider it perfectly.” “in the latter days ye shall consider it.”', 'The same clause stands twice, each after a “whirlwind” on “the head of the wicked.” “Ye” are to consider it.'),
    ('Jer 48:47; 49:39', '“Yet will I bring again the captivity of Moab in the latter days, saith the LORD.” “it shall come to pass in the latter days, that I will bring again the captivity of Elam, saith the LORD.”', 'The phrase closes an oracle about Moab and an oracle about Elam, each with a restoring clause.'),
    ('Ezek 38:8, 16', '“After many days thou shalt be visited: in the latter years thou shalt come into the land that is brought back from the sword,” “it shall be in the latter days, and I will bring thee against my land, that the heathen may know me,”', 'The words are addressed to Gog (38:14–16). “Latter years” and “latter days” both stand; the passage names “my people of Israel” and “my land.”'),
    ('Hos 3:4–5', '“For the children of Israel shall abide many days without a king,” “Afterward shall the children of Israel return, and seek the LORD their God, and David their king; and shall fear the LORD and his goodness in the latter days.”', 'A time of “many days” is followed by “afterward”; the phrase closes the sentence about the return.'),
    ('Dan 2:28–29', '“there is a God in heaven that revealeth secrets, and maketh known to the king Nebuchadnezzar what shall be in the latter days.”', 'Daniel speaks to the king. The phrase stands in a sentence about a dream and a God who “revealeth secrets.”'),
    ('Dan 10:14', '“Now I am come to make thee understand what shall befall thy people in the latter days: for yet the vision is for many days.”', 'The speaker says “I am come” to Daniel. “Thy people” and “many days” stand in one verse.'),
], [0.15, 0.5, 0.35]))
A(('p', '3.3 What the passages state. Isaiah 2:2 and Micah 4:1 state that “in the last days” a mountain is established and that the law and the word go forth from Zion and Jerusalem. Jeremiah 23:20 and 30:24 state that the anger of the LORD will not return until it has done its work and that “in the latter days” the hearers will consider it. Jeremiah 48:47 and 49:39 attach the phrase to the bringing again of the captivity of Moab and of Elam. Ezekiel 38:8 and 38:16 attach “latter years” and “latter days” to a coming against the land; the passage does not name the day of that coming. Hosea 3:5 attaches the phrase to the children of Israel’s return to the LORD and to David their king. Daniel 2:28 and 10:14 attach it to what a dream and a vision show: in the first, what shall be; in the second, what shall befall Daniel’s people.'))
A(('p', '3.4 What they leave unsaid. None gives a date. Isaiah and Micah do not say how the phrase relates to the other prophets’ use of it. Jeremiah 23:20 and 30:24 do not say what “consider it” will mean. Jeremiah 48:47 and 49:39 do not say when the captivities are brought again beyond the phrase itself. Ezekiel 38 does not say how “after many days” and “in the latter years” fit with “in the latter days,” and the study does not name the figures or place the events. Hosea 3:4 gives “many days” and Daniel 10:14 gives “many days,” and neither says how long.'))
A(('call', 'The Words in Hosea 3:4–5',
   'Hosea says that the children of Israel “shall abide many days without a king” and that “afterward” they shall return and seek “the LORD their God, and David their king,” and shall fear him “in the latter days.” The passage names a waiting, a return and a phrase, and gives no date.'))

A(('h1', S4))
A(('p', '4.1 Daniel’s other time words. Daniel uses several wordings that are not “the latter days.” The table lists them. The study reads each in its own verse and does not join them to “the latter days” of Daniel 2:28 and 10:14 unless a verse does.'))
A(('tbl', '', [
    ('Dan 8:17–19', '“Understand, O son of man: for at the time of the end shall be the vision.” “Behold, I will make thee know what shall be in the last end of the indignation: for at the time appointed the end shall be.”', 'The speaker is the one who came near; the words “time of the end,” “last end” and “time appointed” stand in two verses.'),
    ('Dan 8:23', '“And in the latter time of their kingdom, when the transgressors are come to the full, a king of fierce countenance, and understanding dark sentences, shall stand up.”', 'The words are “latter time,” and they are attached to a kingdom. The sentence goes on to speak of a king.'),
    ('Dan 11:35, 40', '“even to the time of the end: because it is yet for a time appointed.” “And at the time of the end shall the king of the south push at him:”', 'The phrase appears twice in one chapter, once with “a time appointed.”'),
    ('Dan 12:4, 9, 13', '“seal the book, even to the time of the end:” “the words are closed up and sealed till the time of the end.” “thou shalt rest, and stand in thy lot at the end of the days.”', 'A sealing “to the time of the end,” and a last verse that says “at the end of the days.”'),
], [0.15, 0.5, 0.35]))
A(('p', '4.2 What the verses state and leave unsaid. Daniel 8:17 and 8:19 say that the vision is “at the time of the end” and name “the last end of the indignation.” Daniel 12:4 and 12:9 say that the book is sealed “to the time of the end.” Daniel 12:13 says “at the end of the days.” The verses do not say that “time of the end” is “the latter days” of 10:14, and they do not say that it is not. They do not date the end. The study does not take up the king of Daniel 8:23 or the kings of chapter 11; Study 74 reports the final-ruler passages side by side.'))
A(('p', '4.3 “The last day” in John. John prints the singular, “the last day,” seven times: four times in John 6 (“I will raise him up at the last day,” 6:39, 40, 44, 54), once for the feast (“In the last day, that great day of the feast,” 7:37), once in Martha’s words (“I know that he shall rise again in the resurrection at the last day,” 11:24) and once in the Lord’s words (“the same shall judge him in the last day,” 12:48). The singular is a different wording from the plural “last days.” The verses do not say that the two are one thing, and they do not say that they are different. John 7:37 uses the words of the last day of the feast.'))
A(('p', '4.4 “Latter day” and “latter end.” Job 19:25 says, “he shall stand at the latter day upon the earth.” The verse is Job’s own statement and uses the singular. The study records it with the singular words of John and draws no doctrine from either.'))

A(('h1', S5))
A(('p', '5.1 The setting. Acts 2 opens at Pentecost. Peter stands with the eleven and speaks to “Ye men of Judaea, and all ye that dwell at Jerusalem” (2:14). He says that the company is not drunken (2:15) and then says, “But this is that which was spoken by the prophet Joel” (2:16). The next verse begins with the words that this study traces.'))
A(('ctbl', '', [
    ['Joel 2:28–29', 'Acts 2:17', 'Observation'],
    ['“And it shall come to pass afterward, that I will pour out my spirit upon all flesh;”', '“And it shall come to pass in the last days, saith God, I will pour out of my Spirit upon all flesh:”', 'The opening differs: “afterward” in Joel, “in the last days, saith God” in Acts.'],
    ['“and your sons and your daughters shall prophesy, your old men shall dream dreams, your young men shall see visions:”', '“and your sons and your daughters shall prophesy, and your young men shall see visions, and your old men shall dream dreams:”', 'The same persons are named; the order of the old men and the young men differs.'],
], [0.37, 0.37, 0.26]))
A(('p', '5.2 What the passage states. Peter says that what the hearers see “is that which was spoken by the prophet Joel” and gives the words “in the last days, saith God.” The speaker of the quotation is “God,” and the persons addressed are men of Judaea and dwellers at Jerusalem. The wording of Joel 2:28 is “afterward”; the wording of Acts 2:17 is “in the last days.” Study 20 sets the two passages side by side across their whole length for the sake of Acts 2:38, and this study records only the one phrase.'))
A(('p', '5.3 What the passage leaves unsaid. It does not say why the opening words differ. It does not say when the last days of Acts 2:17 begin or end. It does not say whether the last days of Acts 2:17 are the same as the last days of Isaiah 2:2 or of 2 Timothy 3:1. Peter’s words “this is that” are recorded as he spoke them, and the passage does not say how much of the words that follow he takes to be present at that hour.'))

A(('h1', S6))
A(('p', '6.1 Six letters, one phrase. Six letters use “last days,” “last time” or “last times,” and each introduces the phrase in a different kind of sentence and with different readers in view. The table sets out what each states. The study reads each letter’s own words about its readers and does not carry one letter’s wording into another. This reading rests on the letters’ own audience markers and setting.'))
A(('tbl', '', [
    ('Heb 1:1–2', '“God, who at sundry times and in divers manners spake in time past unto the fathers by the prophets, Hath in these last days spoken unto us by his Son,”', 'A contrast of “time past” and “these last days”; the verb is “hath … spoken,” in the past.'),
    ('Jas 1:1; 5:1–3', '“to the twelve tribes which are scattered abroad” “Go to now, ye rich men, weep and howl for your miseries that shall come upon you.” “Ye have heaped treasure together for the last days.”', 'The letter names its readers in 1:1; the phrase stands in a sentence to “ye rich men”; the verb is past (“have heaped”).'),
    ('1 Pet 1:1, 5, 20', '“to the strangers scattered throughout Pontus, Galatia, Cappadocia, Asia, and Bithynia,” “ready to be revealed in the last time.” “but was manifest in these last times for you,”', 'Two wordings in one chapter: “the last time” and “these last times.” The first is “ready to be revealed”; the second is “was manifest … for you.”'),
    ('2 Pet 3:1–4', '“Knowing this first, that there shall come in the last days scoffers, walking after their own lusts,” “Where is the promise of his coming?”', 'The verb is future (“shall come”), and the scoffers speak.'),
    ('1 John 2:18', '“Little children, it is the last time: and as ye have heard that antichrist shall come, even now are there many antichrists; whereby we know that it is the last time.”', 'The wording is “the last time,” stated twice; the verb is present (“it is”).'),
    ('Jude 1:17–19', '“remember ye the words which were spoken before of the apostles of our Lord Jesus Christ;” “How that they told you there should be mockers in the last time,”', 'The apostles are said to have “told” the readers; the verb is “should be.”'),
], [0.15, 0.5, 0.35]))
A(('p', '6.2 What the passages state. Hebrews 1:2 says that God “hath in these last days spoken unto us by his Son.” James 5:3 says that the rich “have heaped treasure together for the last days,” and 5:7–8 speaks of “the coming of the Lord.” First Peter 1:5 says that salvation is “ready to be revealed in the last time,” and 1:20 says that the one foreordained “was manifest in these last times for you.” Second Peter 3:3 says that scoffers “shall come in the last days.” First John 2:18 says “it is the last time.” Jude 18 says that the apostles told the readers that “there should be mockers in the last time.”'))
A(('p', '6.3 What the passages leave unsaid. The verbs differ: “hath … spoken,” “have heaped,” “was manifest,” “shall come,” “it is,” “should be.” The study records them as printed and does not reconcile them. The passages do not say that the “last days” of Hebrews 1:2 are the “last days” of James 5:3, and they do not say that they are not. Second Peter 3:3 and Jude 18 both speak of scoffers or mockers who walk after their own lusts, and neither says that the other’s days are meant. First John 2:18 does not say how the words “the last time” relate to the coming of antichrist beyond the sentence itself; the study does not take up that figure, which Study 74 reports. Hebrews 9:26 uses another wording, “now once in the end of the world hath he appeared to put away sin by the sacrifice of himself,” and does not say that “the end of the world” is “the last days.”'))
A(('call', 'What the Verbs Show',
   'The six letters use different verbs with the phrase: “hath spoken” (Hebrews), “have heaped” (James), “was manifest” (1 Peter), “shall come” (2 Peter), “it is” (1 John), “should be” (Jude). The study records each tense and reconciles none.'))

A(('h1', S7))
A(('p', '7.1 Two letters to Timothy. Paul writes to Timothy in both passages. The first speaks of “the latter times” and the second of “the last days.” This reading rests on the letters’ own audience markers and setting.'))
A(('tbl', '', [
    ('1 Tim 4:1–3', '“Now the Spirit speaketh expressly, that in the latter times some shall depart from the faith, giving heed to seducing spirits, and doctrines of devils;”', 'The speaker named is “the Spirit”; the wording is “the latter times”; the verb is “shall depart.”'),
    ('2 Tim 3:1–5', '“This know also, that in the last days perilous times shall come.” “Having a form of godliness, but denying the power thereof: from such turn away.”', 'An instruction to know (“This know also”); the wording is “the last days”; the verb is “shall come”; the passage ends with “from such turn away.”'),
], [0.15, 0.5, 0.35]))
A(('p', '7.2 What the passages state and leave unsaid. In both passages the speaker is Paul, the hearer is Timothy and the verb is future: “shall depart,” “shall come.” First Timothy 4:1 says that the Spirit “speaketh expressly” of this. Second Timothy 3:1–5 lists what men “shall be” and ends with a charge to turn away. Neither passage says that “the latter times” and “the last days” are one period. Neither says how the days relate to those of Acts 2:17, Hebrews 1:2 or 2 Peter 3:3, and neither says when “shall come” begins. The study does not set the words of 2 Timothy 3 beside those of 2 Peter 3 and Jude as if they were one prophecy; it records that the words “last days” and a list of vices stand in each and stops there.'))
A(('p', '7.3 One word to Corinth. First Corinthians 10:11 says of what happened to the fathers, “they are written for our admonition, upon whom the ends of the world are come.” The wording is “the ends of the world,” not “the last days.” The verse does not say that the ends of the world are the last days, and the study records it beside Hebrews 9:26 and does not join them.'))

A(('h1', S8))
A(('p', '8.1 The passages side by side. The table gives each passage, the speaker and hearer, the wording, the verb or sentence that follows and what the passage leaves unsaid.'))
A(('ctbl', '', [
    ['Passage', 'Speaker and hearer', 'Wording and what follows', 'What it leaves unsaid'],
    ['Gen 49:1', 'Jacob to his sons', '“in the last days”; what shall befall them', 'A date; the link to Num 24:14'],
    ['Num 24:14', 'Balaam to Balak', '“in the latter days”; what “this people” shall do', 'A date; who “this people” is beyond the text'],
    ['Deut 4:30; 31:29', 'Moses to Israel', '“in the latter days”; tribulation and a condition; corruption and evil', 'How the two are linked'],
    ['Isa 2:2; Mic 4:1', 'Isaiah and Micah', '“in the last days”; a mountain, the law, the word', 'How the phrase relates to the rest'],
    ['Jer 23:20; 30:24', 'The LORD, in Jeremiah', '“in the latter days ye shall consider it”', 'What “consider” means'],
    ['Jer 48:47; 49:39', 'The LORD, in Jeremiah', '“in the latter days”; captivity brought again', 'The date of the return'],
    ['Ezek 38:8, 16', 'The LORD, to Gog', '“latter years”; “latter days”; a coming against the land', 'The date; the link between the two wordings'],
    ['Hos 3:5', 'The prophet, of Israel', '“afterward”; “in the latter days”; return to the LORD and David their king', 'The length of “many days”'],
    ['Dan 2:28; 10:14', 'Daniel; the messenger', '“in the latter days”; a dream; a vision “for many days”', 'The date; the link to “the time of the end”'],
    ['Acts 2:17', 'Peter to men of Judaea', '“in the last days, saith God”; the Spirit poured out', 'Why the wording differs from Joel; when the days end'],
    ['Heb 1:2; Jas 5:3; 1 Pet 1:5, 20; 2 Pet 3:3; 1 John 2:18; Jude 18', 'Six letters', 'Past, present and future verbs with “last”', 'Whether the days are one period'],
    ['1 Tim 4:1; 2 Tim 3:1', 'Paul to Timothy', '“latter times”; “last days”; “shall depart”; “shall come”', 'Whether the days are one period or the days of Acts 2:17'],
], [0.17, 0.2, 0.37, 0.26]))
A(('p', '8.2 Three readings tested. Three readings are common, and each can be set beside the words. (a) The phrase names one period in every passage. The table shows the phrase in the mouths of Jacob, Balaam, Moses, the prophets, Peter, six letter writers and Paul, with different hearers and different verbs, and no passage states that these are one period. (b) The phrase always names the time that began at Acts 2:17. Acts 2:17 says “in the last days”; it does not say that Genesis 49:1 or Deuteronomy 31:29 is that time, and 2 Peter 3:3 and 2 Timothy 3:1 are future (“shall come”). (c) The phrase always names a time still ahead. Hebrews 1:2 says “hath in these last days spoken,” and 1 John 2:18 says “it is the last time.” Each of the three adds something the text does not state: one period everywhere, a start at Acts 2:17 in every passage, or a time still ahead in every passage. The passages say what each speaker says, and nothing more.'))

A(('h1', 'Conclusion'))
A(('p', 'The Bible uses “the last days / latter days / last time / time of the end” in many places, but the Bible does not give one single meaning for the phrase. Each speaker uses it differently, to different hearers, and for different things that follow. None of the passages join themselves together, and the study refuses to join them. Any reading that tries to unify all these passages goes beyond what the text states.'))

A(('h1', 'Study Summary'))
A(('bul', [
    'The King James Version prints “the last days” eight times and “the latter days” eleven, with near wordings in Ezekiel, Daniel, John, 1 Timothy, 1 Peter, 1 John and Jude.',
    'Jacob, Balaam and Moses each use the phrase in a different sentence, to a different hearer (Genesis 49:1; Numbers 24:14; Deuteronomy 4:30 and 31:29).',
    'Isaiah 2:2 and Micah 4:1 agree on a mountain, the law and the word. Jeremiah, Ezekiel, Hosea and Daniel attach the phrase to other matters.',
    'Acts 2:17 says “in the last days, saith God,” where Joel 2:28 says “afterward.”',
    'The letters use “last” and “latter” wordings with different verbs, and no passage says that another names the same days.',
]))

A(('h1', 'Key Distinctions to Retain'))
A(('bul', [
    'The same English words stand in many passages. Each passage has its own speaker, hearer and sentence. A shared phrase is not a shared period unless a passage says so.',
    '“The latter days,” “the last days,” “the latter times,” “the last time,” “the time of the end” and “the last day” are different wordings. Only a verse can join them, and no verse does.',
    'The verbs differ (“shall befall,” “hath spoken,” “was manifest,” “it is,” “shall come”). Each verb carries its own tense, and the study adds no date.',
]))

A(('h1', 'Scripture-Tracing Exercise'))
A(('p', 'Trace the passages in the order below. For each step, read the verses in their chapter, write who speaks and who is addressed, write what follows the phrase, and write what the passage leaves unsaid.'))
A(('num', [
    'Read Genesis 49:1–2 and Numbers 24:14–20 and write who speaks, who hears and the wording of each.',
    'Read Deuteronomy 4:25–31 and 31:27–29 and write what stands before and after “the latter days” in each.',
    'Read Isaiah 2:1–4 and Micah 4:1–3 and write which words agree and which differ.',
    'Read Jeremiah 23:19–20, 30:23–24, 48:47 and 49:38–39 and write the clause each carries.',
    'Read Ezekiel 38:8, 14–16 and Hosea 3:3–5 and write the wordings used and the people named.',
    'Read Daniel 2:28–29, 8:17–23, 10:14 and 12:4–13 and write each time wording and whom it is spoken to.',
    'Read Acts 2:14–17 beside Joel 2:28–29 and write what the opening words are in each.',
    'Read Hebrews 1:1–2, James 5:1–8, 1 Peter 1:1–5, 20, 2 Peter 3:1–4, 1 John 2:18 and Jude 17–19 and write the verb used with each “last.”',
    'Read 1 Timothy 4:1–3 and 2 Timothy 3:1–5 and write the wording, the verb and what follows.',
]))

A(('h1', 'Review and Discussion Questions'))
A(('num', [
    'How many times does the King James Version print “the last days” and “the latter days,” and in which books?',
    'What does Deuteronomy 4:30 say stands before and after “the latter days,” and how does Deuteronomy 31:29 differ?',
    'Which words agree between Isaiah 2:2 and Micah 4:1, and which differ?',
    'What wording does Joel 2:28 use where Acts 2:17 says “in the last days”?',
    'What verb stands with the phrase in each of Hebrews 1:2, 1 Peter 1:20, 2 Peter 3:3 and 1 John 2:18?',
]))

A(('h1', 'Teaching Outline'))
A(('p', 'I. The wordings. A. “Last days” and “latter days.” B. The near wordings.'))
A(('p', 'II. The Law. A. Genesis 49:1. B. Numbers 24:14. C. Deuteronomy 4:30 and 31:29.'))
A(('p', 'III. The prophets. A. Isaiah 2:2 and Micah 4:1. B. Jeremiah. C. Ezekiel and Hosea. D. Daniel.'))
A(('p', 'IV. Other time words. A. Daniel’s “time of the end.” B. “The last day” in John.'))
A(('p', 'V. Acts 2. A. The hearers. B. Joel’s words and Peter’s.'))
A(('p', 'VI. The letters. A. Hebrews, James and 1 Peter. B. 2 Peter, 1 John and Jude. C. Timothy.'))

A(('h1', 'Guided Further Study'))
A(('p', 'Read each group in context, observe the point named and write one sentence of conclusion.'))
A(('p', 'Group 1: The Law. Read Genesis 49:1, Numbers 24:14 and Deuteronomy 31:29. Observe the speaker and the hearer. Conclude what each says follows the phrase.'))
A(('p', 'Group 2: The prophets. Read Isaiah 2:2, Jeremiah 23:20 and Hosea 3:5. Observe the sentence that carries the phrase. Conclude what each states and leaves unsaid.'))
A(('p', 'Group 3: The New Testament. Read Acts 2:17, Hebrews 1:2 and 2 Timothy 3:1 in their chapters. Observe the verb and the hearers. Conclude what each states of the days.'))

A(('h1', 'Final Synthesis'))
A(('p', 'The Bible uses “the last days” and “the latter days” in many places, and no passage says they all mean one time. Each speaker uses the phrase in their own sentence, to their own hearers, with their own verb. No passage joins them.'))
A(('p', 'Now write it in your own words, in about 250 words:'))
A(('bul', [
    'Say where the KJV uses the phrase.',
    'Name who speaks and who hears in at least five passages.',
    'Set the New Testament verbs side by side and quote them.',
    'End with one sentence: “No passage states that these are one period.”',
]))
