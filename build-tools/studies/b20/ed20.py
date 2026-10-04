from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','DO NOT WEAKEN PETER’S WORDS','ACTS OVERLAP PRINCIPLE','FINAL STUDY CONTROL'}
def apply(els):
    assert T(els[1]).startswith('Acts 2:38 is among the most')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'the prophetic framework Peter himself supplied','the prophetic setting Peter himself supplied')
    rep(els,'Kingdom and restoration framework of Peter','Kingdom and restoration setting of Peter')
    rep(els,'the Acts Overlap framework keep','the Acts Overlap keep')
    rep(els,'“spoken by the prophets” framework','“spoken by the prophets” setting')
    rep(els,'The saving work is God’s work in Christ; Peter is prescribing','The ground of forgiveness is God’s grace, not the rite, and what Peter’s hearers are to believe is what he has just declared: that God has made this Jesus both Lord and Christ (Acts 2:36). Peter is prescribing')
    rep(els,'until the Prophecy Program is suspended at Acts 28.','until Israel’s Prophecy Program is nationally suspended at Acts 28—not canceled, transferred or absorbed. Acts 28 establishes the suspension boundary; it does not by itself establish any further chronology, and this study does not reconstruct one.')
    i=find(els,'Acts 2 occurs before the Mystery Program begins')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    app(els,'That later overlap is important because water baptism',R11)
    k=[i for i,e in enumerate(els) if e['type']=='tbl' and e['rows'][0][:2]==['Passage','Speaker / Audience']][0]
    old=[r[0] for r in els[k]['rows'][1:]]; assert len(old)==9
    Q=lambda t:'“'+t+'”'
    kjv=[Q('[28] And it shall come to pass afterward, that I will pour out my spirit upon all flesh; and your sons and your daughters shall prophesy, your old men shall dream dreams, your young men shall see visions: [29] And also upon the servants and upon the handmaids in those days will I pour out my spirit. [32] And it shall come to pass, that whosoever shall call on the name of the LORD shall be delivered: for in mount Zion and in Jerusalem shall be deliverance, as the LORD hath said, and in the remnant whom the LORD shall call.'),
    Q('[1] In those days came John the Baptist, preaching in the wilderness of Judaea, [2] And saying, Repent ye: for the kingdom of heaven is at hand. [11] I indeed baptize you with water unto repentance: but he that cometh after me is mightier than I, whose shoes I am not worthy to bear: he shall baptize you with the Holy Ghost, and with fire:'),
    Q('[6] When they therefore were come together, they asked of him, saying, Lord, wilt thou at this time restore again the kingdom to Israel? [7] And he said unto them, It is not for you to know the times or the seasons, which the Father hath put in his own power. [8] But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be witnesses unto me both in Jerusalem, and in all Judaea, and in Samaria, and unto the uttermost part of the earth.'),
    Q('[36] Therefore let all the house of Israel know assuredly, that God hath made that same Jesus, whom ye have crucified, both Lord and Christ. [37] Now when they heard this, they were pricked in their heart, and said unto Peter and to the rest of the apostles, Men and brethren, what shall we do? [38] Then Peter said unto them, Repent, and be baptized every one of you in the name of Jesus Christ for the remission of sins, and ye shall receive the gift of the Holy Ghost. [39] For the promise is unto you, and to your children, and to all that are afar off, even as many as the Lord our God shall call.'),
    Q('[19] Repent ye therefore, and be converted, that your sins may be blotted out, when the times of refreshing shall come from the presence of the Lord; [20] And he shall send Jesus Christ, which before was preached unto you: [21] Whom the heaven must receive until the times of restitution of all things, which God hath spoken by the mouth of all his holy prophets since the world began. [26] Unto you first God, having raised up his Son Jesus, sent him to bless you, in turning away every one of you from his iniquities.'),
    Q('[44] While Peter yet spake these words, the Holy Ghost fell on all them which heard the word. [45] And they of the circumcision which believed were astonished, as many as came with Peter, because that on the Gentiles also was poured out the gift of the Holy Ghost. [46] For they heard them speak with tongues, and magnify God. Then answered Peter, [47] Can any man forbid water, that these should not be baptized, which have received the Holy Ghost as well as we? [48] And he commanded them to be baptized in the name of the Lord. Then prayed they him to tarry certain days.'),
    Q('[2] He said unto them, Have ye received the Holy Ghost since ye believed? And they said unto him, We have not so much as heard whether there be any Holy Ghost. [3] And he said unto them, Unto what then were ye baptized? And they said, Unto John’s baptism. [4] Then said Paul, John verily baptized with the baptism of repentance, saying unto the people, that they should believe on him which should come after him, that is, on Christ Jesus. [5] When they heard this, they were baptized in the name of the Lord Jesus. [6] And when Paul had laid his hands upon them, the Holy Ghost came on them; and they spake with tongues, and prophesied.'),
    Q('[12] For as the body is one, and hath many members, and all the members of that one body, being many, are one body: so also is Christ. [13] For by one Spirit are we all baptized into one body, whether we be Jews or Gentiles, whether we be bond or free; and have been all made to drink into one Spirit.'),
    Q('[4] There is one body, and one Spirit, even as ye are called in one hope of your calling; [5] One Lord, one faith, one baptism, [6] One God and Father of all, who is above all, and through all, and in you all.')]
    obs=['Who speaks and to whom? Note “all flesh,” the signs given, and “in mount Zion and in Jerusalem.”',
    'Who speaks? Note “the kingdom of heaven is at hand” and baptism “with the Holy Ghost, and with fire.”',
    'Who asks, and what do they ask about Israel? Note what Jesus withholds and what He promises.',
    'Who is addressed in verse 36? Note “Repent, and be baptized,” “for the remission of sins,” and “the promise is unto you.”',
    'Note “times of refreshing,” “restitution of all things,” and “Unto you first.”',
    'Who is listening, and what is given before baptism?',
    'Note the disciples’ answer in verse 2 and what follows the laying on of hands.',
    'Who is addressed? Note “by one Spirit are we all baptized into one body.”',
    'Note “one body,” “one Spirit,” and “one baptism.”']
    rows=[['Verse','KJV text','What to observe']]+[[old[n],kjv[n],obs[n]] for n in range(9)]
    instr=els[k-1]; assert T(instr).startswith('Read the following passages in order')
    els[k-1]=mk('body',[['The table sets each passage in the King James Version beside a cue to trace. '+T(instr),False,False]])
    els[k]=dict(type='tbl',rows=rows,xs=[[0,120],[120,430],[430,640]])
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
