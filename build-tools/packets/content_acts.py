# DRAFT for publisher approval.
BOOK = "Acts"
TESTAMENT = "New Testament"
GENRE = "history"
SUBTITLE = "The Kingdom Witness, the Calling of Paul, and the Overlap of Two Programs"
SECTIONS = []
def S(n, t, *blocks): SECTIONS.append((n, t, list(blocks)))
P = lambda x: ("p", x)
L = lambda *xs: ("ul", list(xs))
H = lambda x: ("h3", x)
TBL = lambda head, rows, widths: ("table", head, rows, widths)
OL = lambda *xs: ("ol", list(xs))
OLR = lambda *xs: ("olr", list(xs))
BOX = lambda lead, text: ("box", lead, text)
ISR = 'Israel / Kingdom / Prophecy Explicit Truth'

S(1, 'Book Overview (Program-Aware)',
  P('Acts records what the risen Lord did through his witnesses after the resurrection. It opens with the Lord “speaking of the things pertaining to the kingdom of God” and the disciples’ question, “wilt thou at this time restore again the kingdom to Israel?” (Acts 1:3, 6). It follows the witness at Jerusalem, the word carried to Samaria, the calling of Saul, the word going to Cornelius, the council at Jerusalem, Paul’s journeys and his voyage to Rome, and it ends with Paul “preaching the kingdom of God, and teaching those things which concern the Lord Jesus Christ” (Acts 28:31).'),
  BOX('Program Identity:', 'Acts carries both programs. Chapters 1–8 belong to Israel’s Prophecy Program. With chapter 9 Paul’s ministry begins, and chapters 9–28 are the overlap: Paul’s gospel forms the Body while Israel’s Prophecy Program remains operative until its national suspension at Acts 28. Events in Acts 9–28 are reported as written and are not assigned to a single program.'))

S(2, 'Narrative Flow of Acts',
  H('Movement 1 — The Witness at Jerusalem (Chs. 1–7)'),
  P('The Lord speaks of the kingdom of God, the disciples ask about the kingdom to Israel, the Holy Ghost fills them at Pentecost, and Peter tells “all the house of Israel” that God has made Jesus “both Lord and Christ” (Acts 1:3, 6; 2:4, 36).'),
  H('Movement 2 — Judea and Samaria (Ch. 8)'),
  P('Those who were scattered abroad go “every where preaching the word,” Philip preaches Christ in Samaria, and the apostles at Jerusalem send Peter and John (Acts 8:4–5, 14, 17).'),
  H('Movement 3 — Saul Called (Ch. 9)'),
  P('The Lord speaks to Saul on the way, calls him “a chosen vessel unto me, to bear my name before the Gentiles, and kings, and the children of Israel,” and sends Ananias to him (Acts 9:4, 15, 17).'),
  H('Movement 4 — Cornelius and the Council (Chs. 10–15)'),
  P('Peter says that God is “no respecter of persons,” the Holy Ghost is poured out on the Gentiles also, and Paul and Barnabas rehearse how God “had opened the door of faith unto the Gentiles.” The chapters are reported as written, as events of the overlap (Acts 10:34, 45; 11:19; 14:27).'),
  H('Movement 5 — Paul Sent (Chs. 13–20)'),
  P('The Holy Ghost separates Barnabas and Saul, Paul reasons in the synagogues out of the scriptures, turns locally to the Gentiles, and tells the Ephesian elders that he counts his life not dear so that he might “testify the gospel of the grace of God” (Acts 13:2, 46; 17:2; 18:6; 20:24).'),
  H('Movement 6 — Jerusalem to Rome (Chs. 21–28)'),
  P('Paul is carried to Rome, expounds and testifies the kingdom of God to the Jews there, and reports the word of the Holy Ghost by Esaias. The book reports his saying that “the salvation of God is sent unto the Gentiles” and closes with him dwelling two whole years preaching and teaching (Acts 28:23, 25, 28, 30–31). Acts 28 is the national suspension of Israel’s Prophecy Program; the book itself reports the scene as written.'))

S(3, 'Program Themes in Acts',
  H('1. The Kingdom Question'),
  P('The Lord speaks of “the things pertaining to the kingdom of God,” and the disciples ask whether he will at this time “restore again the kingdom to Israel” (Acts 1:3, 6).'),
  H('2. The Witness to Israel'),
  P('Peter tells “all the house of Israel” that God has made that same Jesus “both Lord and Christ,” and that God exalted him “to give repentance to Israel, and forgiveness of sins” (Acts 2:36; 5:31).'),
  H('3. The Times of Refreshing and Restitution'),
  P('“Repent ye therefore, and be converted… when the times of refreshing shall come from the presence of the Lord,” and the heaven must receive Jesus “until the times of restitution of all things, which God hath spoken by the mouth of all his holy prophets” (Acts 3:19, 21). This belongs to Israel’s program and does not transfer to the Body.'),
  H('4. The Chosen Vessel'),
  P('The Lord calls Saul “a chosen vessel unto me, to bear my name before the Gentiles, and kings, and the children of Israel,” and later sends him “far hence unto the Gentiles” (Acts 9:15; 22:21).'),
  H('5. The Gospel of the Grace of God'),
  P('Paul counts his life not dear so that he might finish his course and “the ministry, which I have received of the Lord Jesus, to testify the gospel of the grace of God” (Acts 20:24).'),
  H('6. Two Programs Running Together'),
  P('During Acts 9–28 the remnant remains Israel’s prophetic believing company, and the Body remains the Mystery new creation. They coexist historically but never merge in identity, membership, calling, covenant, gospel, hope, or destiny. Concurrency is operational, not transformational.'))

S(4, 'Christ in Acts: The Prophetic Trajectory',
  H('1. Both Lord and Christ'),
  P('“God hath made that same Jesus, whom ye have crucified, both Lord and Christ” (Acts 2:36).'),
  H('2. A Prince and a Saviour'),
  P('“Him hath God exalted with his right hand to be a Prince and a Saviour, for to give repentance to Israel, and forgiveness of sins” (Acts 5:31).'),
  H('3. The Times of Restitution'),
  P('“Whom the heaven must receive until the times of restitution of all things” (Acts 3:21).'),
  H('4. The Lord Who Spoke to Saul'),
  P('“Saul, Saul, why persecutest thou me?” is the voice Saul hears on the way (Acts 9:4).'),
  H('5. The Lord Jesus Who Gave the Ministry'),
  P('Paul speaks of “the ministry, which I have received of the Lord Jesus” (Acts 20:24), and recalls “the words of the Lord Jesus, how he said, It is more blessed to give than to receive” (Acts 20:35).'),
  H('6. Preached to the Close'),
  P('Paul is “teaching those things which concern the Lord Jesus Christ, with all confidence, no man forbidding him” (Acts 28:31), reported as written.'))

S(5, 'Israel and the Body in Acts',
  P('Acts 1–8 is the Prophecy Program. Acts 9–28 is the overlap, in which Paul’s ministry forms the Body while Israel’s program remains operative until its national suspension at Acts 28. Acts reinforces Israel’s:'),
  L('kingdom hope and question (Acts 1:6)', '“all the house of Israel” addressed at Pentecost (Acts 2:36)', 'repentance given to Israel (Acts 5:31)', 'times of restitution spoken by the prophets (Acts 3:21)', 'covenant made with the fathers (Acts 3:25)'),
  P('During the overlap, the circumcision apostleship ministers to Israel under the Prophecy Program, and Paul’s gospel forms the Body; the two operate concurrently and never merge, transfer or absorb one another.'))

S(6, 'Body-of-Christ Distinctions',
  P('Acts reports Paul’s ministry; the Body’s doctrine is set out in Paul’s letters. In Acts:'),
  L('Paul is called to bear the Lord’s name “before the Gentiles, and kings, and the children of Israel” (Acts 9:15)', 'Paul’s ministry is to “testify the gospel of the grace of God” (Acts 20:24)', 'the word of God’s grace is able to build up the saints (Acts 20:32)'),
  P('Paul’s commission never changes: he is the apostle of the Gentiles, and his own gospel is the gospel of the grace of God. When he reasons in the synagogues from Israel’s Scriptures, he proclaims Israel’s Messiah and kingdom hope to Israel, whose prophetic program remained operative until its national suspension at Acts 28. That is audience-specific proclamation, not a second gospel and not a change of commission; it does not make Paul a Prophecy apostle, and it does not make his hearers members of the Body by that message. Paul’s synagogue preaching was audience-specific, not commission-specific.'),
  P('Fillings, signs and miraculous events in Acts 9–28 are recorded in settings shaped by Israel’s Prophecy Program, which remained operative throughout Acts 9–28 even as the Mystery Program began. Acts 9–28 is the overlap; where Paul or his companions are the ones filled or working signs, the book is reported as written and the event is not assigned to a single program. With the national suspension of Israel’s Prophecy Program at Acts 28, the sign‑program associated with Israel ceases programmatically. Signs do not continue into the Mystery Program.'),
  P('Acts does not make the Body Israel, place the Body in Israel’s covenants, or turn the kingdom witness of chapters 1–8 into the Body’s calling.'))

S(7, 'Program-Specific Truths Table',
  TBL(['Category', 'Truth Revealed in Acts', 'Program Identity', 'Scripture'], [['The Kingdom Question', 'The disciples ask whether the kingdom will be restored to Israel.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Acts 1:6'], ['The House of Israel', 'Peter addresses all the house of Israel at Pentecost.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Acts 2:36'], ['Restitution of All Things', 'The times of restitution are spoken by the prophets and await the Lord’s coming from heaven.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Acts 3:21'], ['The Covenant with the Fathers', 'The hearers are called children of the prophets and of the covenant made with Abraham.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Acts 3:25'], ['Repentance to Israel', 'Christ is exalted to give repentance to Israel and forgiveness of sins.', 'Israel / Kingdom / Prophecy Explicit Truth', 'Acts 5:31'], ['The Chosen Vessel', 'Saul is called to bear the Lord’s name before the Gentiles, kings and the children of Israel.', 'Body of Christ (Pauline) Truth', 'Acts 9:15'], ['Sent to the Gentiles', 'The Lord sends Paul far hence unto the Gentiles.', 'Body of Christ (Pauline) Truth', 'Acts 22:21'], ['The Gospel of the Grace of God', 'Paul’s ministry is to testify the gospel of the grace of God.', 'Body of Christ (Pauline) Truth', 'Acts 20:24'], ['The Word of His Grace', 'The word of God’s grace is able to build up the saints.', 'Body of Christ (Pauline) Truth', 'Acts 20:32']], [20, 34, 26, 20]))

S(8, 'Universal Truths Table (All People, All Time)',
  TBL(['Universal Truth', 'Description', 'Scripture'], [['Creator of All', 'God made the world and all things in it. “God that made the world and all things therein, seeing that he is Lord of heaven and earth.”', 'Acts 17:24'], ['In Him We Live', 'Life, movement and being are in God. “For in him we live, and move, and have our being.”', 'Acts 17:28'], ['No Respecter of Persons', 'God shows no partiality. “God is no respecter of persons.”', 'Acts 10:34'], ['Searching the Scriptures', 'The Bereans received the word with readiness and tested it daily. “searched the scriptures daily, whether those things were so.”', 'Acts 17:11'], ['Giving', 'The Lord’s saying is recalled: giving is more blessed than receiving. “It is more blessed to give than to receive.”', 'Acts 20:35'], ['Supporting the Weak', 'Labouring so as to support the weak. “so labouring ye ought to support the weak.”', 'Acts 20:35']], [28, 48, 24]))

S(9, 'Program-Safe Application Grid',
  BOX('Why This Section Exists', 'The tables in Sections 7 and 8 help us see clearly what belongs to Israel alone and what truths apply to all people in all ages. This section gently shows how those universal truths can shape our walk with God today. These are not Israel’s kingdom promises or the signs of the overlap; they are timeless truths rooted in God’s character.'),
  P('Drawn only from universal truths, never from Israel’s covenant, land or kingdom, and without turning the events of the overlap into commands. The Body of Christ should:'),
  OL('<b>Search the scriptures</b> — Test what is taught daily (Acts 17:11).', '<b>Honour the Creator</b> — In him we live, and move, and have our being (Acts 17:28).', '<b>Show no partiality</b> — God is no respecter of persons (Acts 10:34).', '<b>Give</b> — It is more blessed to give than to receive (Acts 20:35).', '<b>Support the weak</b> — Labour so as to help (Acts 20:35).'))

S(10, 'Teaching Outline for Acts',
  P('<i>Teacher-ready, movement-based outline</i>'),
  OLR('The Witness at Jerusalem (Chs. 1–7) — The kingdom question and the house of Israel. <i>(Acts 1:3, 6; 2:4, 36; 3:19, 21; 5:31)</i>', 'Judea and Samaria (Ch. 8) — The word scattered abroad. <i>(Acts 8:4–5, 14, 17)</i>', 'Saul Called (Ch. 9) — The chosen vessel. <i>(Acts 9:4, 15, 17)</i>', 'Cornelius and the Council (Chs. 10–15) — No respecter of persons. <i>(Acts 10:34, 45; 14:27)</i>', 'Paul Sent (Chs. 13–20) — The gospel of the grace of God. <i>(Acts 13:2, 46; 17:2; 18:6; 20:24, 32)</i>', 'Jerusalem to Rome (Chs. 21–28) — Preaching and teaching. <i>(Acts 28:23, 25, 28, 30–31)</i>'))

S(11, "Companion Usage and Study Suggestions",
  H("How to Use This Companion in Personal Study"),
  P("This Companion is designed to walk alongside you as you read Acts, helping you see both the way the book carries two programs and the timeless truths rooted in God’s character. Use it slowly, chapter by chapter, letting the narrative movements, themes, and truths deepen your understanding. The Program-Safe Applications will guide your heart toward the scriptures, giving, and showing no partiality, drawn from universal truths, without turning the kingdom witness of Israel’s program or the signs of the overlap into commands for the Body."),
  H("How to Use This Companion in Small Groups or Classes"),
  P("This Companion provides a clear, structured framework that makes teaching Acts simple and accessible. Each section gives you ready-to-use material: narrative movements for overview, program themes for doctrinal clarity, universal truths for discussion, and a pastoral teaching outline for weekly lessons. Use the table to help your group see which truths belong to Israel in chapters 1–8, which belong to Paul’s ministry, and which hold for all people, and use the Program-Safe Application Grid to foster meaningful, Christ-centered conversation."),
  H("How This Companion Fits Within the Acts Overlap Theology Series"),
  P("This Companion is part of a larger series designed to help believers read every book of Scripture without blurring God’s prophetic program for Israel and His mystery program for the Body of Christ. Within the Acts Overlap framework, Acts is the book of the overlap: it records Israel’s kingdom witness and the beginning of Paul’s ministry side by side. This Companion shows you how to keep each in its place while drawing out the truths that apply to all believers in every age."))
