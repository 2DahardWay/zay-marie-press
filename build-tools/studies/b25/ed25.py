from edcommon import *
KEEP={'STUDY GOAL','INTERPRETIVE CONTROL','KEY DISTINCTION','FUNCTION OF THE SIGNS','OVERLAP CONTROL'}
R19="Salvation is always by faith and never by merit; what the commission asks of its hearers is the response God revealed within that program, and baptism is a requirement of that program, not a ground of salvation and not a requirement placed on the Body."
def apply(els):
    assert T(els[1]).startswith('Mark 16:16–18 is among')
    els[1]=mk('body',[['By the end of this study, you should be able to:',False,False]])
    rep(els,'The Framework names Matthew 28:18–20, Luke 24:47, and Acts 1:8 as the Twelve’s Kingdom Commission;','Matthew 28:18–20, Luke 24:47, and Acts 1:8 are the Twelve’s Kingdom Commission;')
    rep(els,'That is this study’s interpretive reading, not a separate Framework ruling.','That is this study’s interpretive reading.')
    rep(els,'The Framework tests any sign by','Any sign is tested by')
    rep(els,'The Acts Overlap framework provides','The Acts Overlap provides')
    rep(els,'The framework also prevents','The Acts Overlap also prevents')
    i=find(els,'That does not mean water itself possesses saving power')
    ins_after_idx(els,i,R19)
    i=find(els,'Acts 9 introduces Paul and the beginning of the Mystery program')
    ins_after_idx(els,i,R17); ins_after_idx(els,i,OVERLAP)
    i=find(els,'They certainly demonstrate divine authorization')
    ins_after_idx(els,i,R11)
    app(els,'This is an important diagnostic principle',R18S)
    k=[n for n,e in enumerate(els) if e['type']=='para' and e['kind']=='num' and ' 9. What does the positive clause' in T(e)]
    assert len(k)==1; del els[k[0]]
    runin_extras(els,KEEP); number_outline(els); glyphs(els)
    return els
