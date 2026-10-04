from edcommon import *
import re
KEEP={'KEY DISTINCTION','AUDIENCE MATTERS','ACTS OVERLAP FOUNDATION','NON-TRANSFER PRINCIPLE','THE ANSWER IN ONE SENTENCE'}
SUSP="nationally suspended—not canceled, transferred or absorbed"
SEQ="Acts 28 establishes the suspension boundary; that the Kingdom gospel is proclaimed again rests on Matthew 24:14 and the prophetic passages traced here, not on Acts 28 alone."
def setp(els,prefix,new):
    i=find(els,prefix); els[i]['segs']=[[new,False,False]]; return i
def apply(els):
    assert T(els[0])=='The Gospel of the Kingdom' and T(els[6])=='What You Will Learn in This Study'
    del els[0:6]
    assert T(els[2]).startswith('By the end of the study')
    els[2]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    assert all(els[k]['kind']=='bul' for k in range(3,13)) and T(els[13])=='Study Outline'
    wy=['Trace the Kingdom through Isaiah, Jeremiah, Daniel and the Gospel accounts, noting what each says about the King, the people and the throne.',
    'Follow the “at hand” announcement through John, Jesus and the Twelve, and record to whom each was sent.',
    'Read Acts 1–3 for what Peter says to Israel about repentance and the restitution of all things, and note where Acts 9 and Acts 28 mark change.',
    'Place Matthew 24:14 within its own prophetic setting before comparing it with Paul’s message.',
    'Examine Paul’s synagogue ministry by its audience, its source and his commission.',
    'Separate salvation by faith from the content of faith and from program-specific requirements, and compare the two gospels without merging their audiences, promises or commissions.']
    els[3:13]=[mk('bul',[[t,False,False]]) for t in wy]
    a=find(els,'Study Outline')  # h1
    b=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e).startswith('Introduction')][0]
    so=['Trace the Kingdom through Isaiah, Jeremiah and Daniel before it is announced as “at hand”.',
    'Follow the same announcement through John, Jesus and the Twelve, and identify its audience.',
    'Place repentance and Kingdom responsibility inside Israel’s prophetic setting.',
    'Follow Israel’s appeal past the Cross through Acts 1–3, and mark Acts 9 and Acts 28.',
    'Read Matthew 24:14 in its prophetic setting.',
    'Handle Paul’s synagogue ministry by its audience and his commission.',
    'Separate salvation by faith from the content of faith and from program-specific requirements.',
    'Compare the Gospel of the Kingdom and the Gospel of the Grace of God without merging them.']
    els[a+1:b]=[mk('bul',[[t,False,False]]) for t in so]
    # Teaching Outline: strip roman numerals
    ta=[k for k,e in enumerate(els) if P(e) and e['kind']=='h1' and T(e).startswith('Teaching Outline')][0]
    k=ta+1
    while els[k]['kind']=='body' and re.match(r'^[IVX]+\. ',T(els[k])):
        els[k]=mk('bul',[[re.sub(r'^[IVX]+\. ','',T(els[k])),False,False]]); k+=1
    setp(els,'Compare the Gospels —','Compare the Gospels — Distinguish audience, content of faith, promises, and commission.')
    setp(els,'Handle Paul Carefully —','Handle Paul Carefully — Distinguish Paul’s one Pauline apostleship from his audience-specific proclamation to Israel.')
    # Rule 19
    rep(els,'Repentance, baptism, and other Kingdom requirements do not become the meritorious ground of salvation. The ground remains God’s grace and the finished work of Christ; the required response reflects the content and obligations God had revealed to Israel.','Salvation is always by faith and never by merit. Repentance, baptism, and other Kingdom requirements are program-specific responsibilities, never the ground of salvation and never Pauline faith-alone doctrine, and they do not transfer to the Body. The required response reflects the content and obligations God had revealed to Israel.')
    setp(els,'At this point, keep two questions separate','At this point, keep two questions separate: What response did God require from the people under that program? And what content of faith had God revealed to them? The first question concerns revealed responsibility; the second concerns the content of faith. Keeping them distinct prevents a required response from being mistaken for the meritorious basis upon which God saves.')
    setp(els,'Program-specific response and Kingdom responsibility','Program-specific response and Kingdom responsibility must not be confused with the ground of salvation. Later in this study we will distinguish salvation by faith, the content of faith, and program-specific requirements.')
    setp(els,'9. Two Gospel Messages','9. Salvation by Faith — The Content of Faith Differs by Program')
    setp(els,'At this point an important question','At this point an important question must be answered directly. If the Gospel of the Kingdom and the Gospel of the Grace of God differ in audience and revealed content, does salvation rest on human merit in either one? No. Salvation is always by faith and never by merit.')
    setp(els,'The ground of salvation is always','No sinner in any program supplies the meritorious basis of salvation. What differs is the content of faith: the content is what God had revealed within each program. Prophecy saints before the Cross, such as Abraham, Moses and David, were saved by believing the content God had revealed to them—not Pauline revelation, and not the finished work of Christ, which had not yet been revealed.')
    setp(els,'But the content of faith is determined','Israel under the Prophecy Program was accountable to the revelation and covenantal responsibilities God had given to Israel. The Body of Christ is saved by believing Pauline revelation, the gospel of the grace of God, through faith alone.')
    setp(els,'Program-specific requirements must therefore','Program-specific requirements must therefore be distinguished from salvation by faith. Repentance, baptism, covenant obligations, Kingdom entrance requirements, or other instructions must be interpreted according to the people and program to which God assigned them; they are never the ground of salvation, never Pauline faith-alone doctrine, and they do not transfer to the Body.')
    setp(els,'1) What is the ground upon which God saves?','1) How is a person saved? By faith, never by merit.  2) What content had God revealed for faith at that point?  3) What program-specific requirements governed the people being addressed? Confusing these questions produces unnecessary contradictions.')
    setp(els,'This distinction allows us to preserve both truths','This distinction allows us to preserve both truths at once: the Gospel of the Kingdom and the Gospel of Grace are not the same message, yet in neither does salvation rest on human merit. The content of faith is what God revealed within each program, and their revealed content and programmatic audience differ.')
    setp(els,'The comparison does not establish two meritorious','The comparison does not establish two meritorious grounds of salvation. It shows why the interpreter must distinguish the content God had revealed for faith in each setting from the program-specific response required of the audience being addressed.')
    rep(els,'while accomplishing salvation through the same finished work of Christ.','while salvation remains by faith and never by merit.')
    rep(els,'Both ultimately rest upon the finished work of Christ, but they differ in revealed content, programmatic audience, promises, and commission.','They differ in revealed content, programmatic audience, promises, and commission, and in neither does salvation rest on merit.')
    setp(els,'The Gospel of the Kingdom and Gospel of Grace share','Salvation is always by faith and never by merit, but the content of faith differs: what God revealed within each program governs the Gospel of the Kingdom and the Gospel of Grace.')
    rep(els,'Ground vs. Content:','Faith vs. Content:')
    rep(els,'The finished work of Christ is the ground of salvation; the content of faith is determined by revelation.','Salvation is by faith, never by merit; the content of faith is what God revealed within each program.')
    rep(els,'What is shared in the saving ground?','How does salvation by faith, never by merit, apply in each message?')
    rep(els,'the ground/content distinction in salvation','the distinction between salvation by faith and the content of faith')
    rep(els,'between the ground of salvation and the content of faith?','between salvation by faith and the content of faith?')
    n=0
    for e in els:
        if e['type']=='tbl':
            for r in e['rows']:
                if r[0]=='Shared ground': r[:]=['Content of faith','What God revealed within Prophecy','Pauline revelation, the gospel of the grace of God']; n+=1
    assert n==1
    # Rule 18
    setp(els,'Yet Israel’s Prophecy Program remained operative',R18)
    setp(els,'The audience, setting, and content matter.','The audience, setting, and content matter. Paul speaks to Jews from Israel’s Scriptures about Israel’s promised Messiah. Speaker identity does not override program identity. '+R18S)
    setp(els,'Paul may communicate previously revealed','When Paul proclaims Israel’s Messiah and kingdom hope to Israel, that proclamation does not become Mystery doctrine, does not transfer Israel’s obligations to the Body, and does not make Paul an administrator of Israel’s Prophecy Program.')
    setp(els,'Paul has one Pauline apostleship and commission. His communication','Paul has one Pauline apostleship and commission. His proclamation of Israel’s Messiah to Israel from her Scriptures does not make him a Prophecy apostle or transfer that message to the Body.')
    rep(els,'Paul may proclaim Prophecy truth to Israel without possessing the Twelve’s Kingdom Commission.','Paul may proclaim Israel’s Messiah to Israel from her Scriptures without possessing the Twelve’s Kingdom Commission.')
    # Acts 28
    rep(els,'the national judicial suspension point is Acts 28.','Israel’s Prophecy Program was nationally suspended at Acts 28.')
    rep(els,'The later national suspension at Acts 28 therefore does not cancel the prophetic Kingdom.','At Acts 28 Israel’s Prophecy Program was %s, so the prophetic Kingdom stands.'%SUSP)
    i=find(els,'When God resumes His prophetic purpose'); els[i]['segs'][0][0]=SEQ+' '+els[i]['segs'][0][0] if False else els[i]['segs'][0][0]+' '+SEQ
    setp(els,'Israel’s Prophecy Program reaches its national judicial suspension point at Acts 28.','At Acts 28 Israel’s Prophecy Program was %s. The promises themselves stand.'%SUSP)
    rep(els,'At Acts 28 Israel’s Prophecy Program reaches its national judicial suspension point. Suspension is not cancellation: Israel remains','At Acts 28 Israel’s Prophecy Program was %s. Israel remains'%SUSP)
    setp(els,'Acts 28 suspends Israel’s active Prophecy Program nationally;','At Acts 28 Israel’s Prophecy Program was nationally suspended (not canceled, transferred or absorbed); Israel’s future promises stand.')
    rep(els,'Acts 28 suspends Israel’s active Prophecy Program nationally; it does not abolish Israel’s prophetic future.','At Acts 28 Israel’s Prophecy Program was nationally suspended (not canceled, transferred or absorbed); Israel’s prophetic future stands.')
    # overlap + R17 once, before the Acts Overlap Foundation callout
    ci=[k for k,e in enumerate(els) if P(e) and e['kind']=='ctitle' and T(e)=='ACTS OVERLAP FOUNDATION'][0]
    ins_after_idx(els,ci-1,OVERLAP+' '+R17)
    for e in els:
        if P(e):
            t=T(e)
            for bad in ['finished work','judicial suspension','shared ground','Shared ground','saving ground','Prophecy truth','supplied the saving']:
                assert bad not in t or 'not yet been revealed' in t,(bad,t[:90])
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
