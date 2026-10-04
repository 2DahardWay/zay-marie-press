from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','PROPHECY REMAINS PROPHECY','ACTS OVERLAP PRINCIPLE','FINAL DOCTRINAL PRINCIPLE'}
def apply(els):
    assert T(els[1]).startswith('Acts 15 records a decisive meeting')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    app(els,'Peter’s reference is to Cornelius','The Gentiles who appear in that account belong to prophetic fulfillment, not to the Body, and their presence implies no Body membership.')
    i=find(els,'Israel’s Prophecy Program began before Acts 9')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    k=[i for i,e in enumerate(els) if e['type']=='tbl' and e['rows'][0]==['Passage','Trace This Question']][0]
    old=els[k]['rows'][1:]; assert len(old)==7
    Q=lambda t:'“'+t+'”'
    kjv=[Q('[1] And certain men which came down from Judaea taught the brethren, and said, Except ye be circumcised after the manner of Moses, ye cannot be saved. [5] But there rose up certain of the sect of the Pharisees which believed, saying, That it was needful to circumcise them, and to command them to keep the law of Moses.'),
    Q('[8] And God, which knoweth the hearts, bare them witness, giving them the Holy Ghost, even as he did unto us; [9] And put no difference between us and them, purifying their hearts by faith. [10] Now therefore why tempt ye God, to put a yoke upon the neck of the disciples, which neither our fathers nor we were able to bear? [11] But we believe that through the grace of the Lord Jesus Christ we shall be saved, even as they.'),
    Q('Then all the multitude kept silence, and gave audience to Barnabas and Paul, declaring what miracles and wonders God had wrought among the Gentiles by them.'),
    Q('[14] Simeon hath declared how God at the first did visit the Gentiles, to take out of them a people for his name. [15] And to this agree the words of the prophets; as it is written, [16] After this I will return, and will build again the tabernacle of David, which is fallen down; and I will build again the ruins thereof, and I will set it up: [17] That the residue of men might seek after the Lord, and all the Gentiles, upon whom my name is called, saith the Lord, who doeth all these things.'),
    Q('[19] Wherefore my sentence is, that we trouble not them, which from among the Gentiles are turned to God: [20] But that we write unto them, that they abstain from pollutions of idols, and from fornication, and from things strangled, and from blood. [21] For Moses of old time hath in every city them that preach him, being read in the synagogues every sabbath day.'),
    Q('[28] For it seemed good to the Holy Ghost, and to us, to lay upon you no greater burden than these necessary things; [29] That ye abstain from meats offered to idols, and from blood, and from things strangled, and from fornication: from which if ye keep yourselves, ye shall do well. Fare ye well.'),
    Q('[7] But contrariwise, when they saw that the gospel of the uncircumcision was committed unto me, as the gospel of the circumcision was unto Peter; [8] (For he that wrought effectually in Peter to the apostleship of the circumcision, the same was mighty in me toward the Gentiles:) [9] And when James, Cephas, and John, who seemed to be pillars, perceived the grace that was given unto me, they gave to me and Barnabas the right hands of fellowship; that we should go unto the heathen, and they unto the circumcision.')]
    rows=[['Verse','KJV text','What to observe']]+[[o[0],kjv[n],o[1]] for n,o in enumerate(old)]
    instr=els[k+1]; assert T(instr).startswith('For each passage, record')
    lead=mk('body',[['The table sets each passage in the King James Version beside the question to trace. '+T(instr),False,False]])
    els[k:k+2]=[lead,dict(type='tbl',rows=rows,xs=[[0,120],[120,430],[430,640]])]
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
