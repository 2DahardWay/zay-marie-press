# Text of the Parable Study Template and its Worked Example (publisher's wording, 2026-10-17).
# Each section: (heading, [items]). Item kinds:
#   ("field", label, answer)            one-line field
#   ("box", prompt_label, hint, answer, height)   labelled writing box (answer = list of lines/bullets or None)
#   ("note", text)                      plain paragraph
#   ("rule", text)                      bold-lead rule line
TEMPLATE_TITLE = "PARABLE STUDY TEMPLATE"
TEMPLATE_SUB = "A Guided Worksheet for Reading Any Parable in Its Gospel Setting"
TEMPLATE_NOTE = "(Free companion resource for all Parables · Digital Studies)"
EXAMPLE_TITLE = "PARABLE STUDY TEMPLATE — WORKED EXAMPLE"
EXAMPLE_SUB = "Example: The Wedding Banquet (Matthew 22:1–14)"

def T():
    return [
 ("1. Passage Information", [
   ("field","Parable Title:",None),("field","Gospel Passage:",None),("field","Parallel Passages (if any):",None)]),
 ("2. Audience & Occasion", [
   ("box","A. Who is Jesus addressing?","(Disciples? Crowds? Pharisees? Scribes? Specific individuals?)",None,66),
   ("box","B. What occasion, question, or complaint is He answering?",None,None,66)]),
 ("3. The Comparison Jesus Supplies", [
   ("box","A. What is the comparison?","(“The Kingdom is like…”, “A man…”, “A father…”, “A master…”)",None,54),
   ("box","B. What movement does the story follow?","(Sequence of events — no allegorizing beyond this movement.)",None,96)]),
 ("4. What Jesus Names vs. What He Leaves Unnamed", [
   ("box","A. Elements Jesus explicitly identifies:","(Characters, actions, outcomes He names.)",None,84),
   ("box","B. Elements Jesus does not identify:","(Characters or symbols the text does not assign.)",None,84),
   ("rule","Rule:","Do not assign identities Jesus does not name.")]),
 ("5. Boundaries of the Parable", [
   ("box","A. What belongs to this parable only?","(Keep it in its own setting — no merging separate stories.)",None,60),
   ("box","B. What similar parables must remain separate?","(e.g., Treasure ≠ Pearl, Dragnet ≠ Wheat & Weeds, Thief ≠ Ten Virgins ≠ Wedding Banquet)",None,72)]),
 ("6. The Stated Point", [
   ("box","A. What point does Jesus make in the text itself?","(What He says at the end, or what the comparison communicates.)",None,72),
   ("box","B. What the parable does not say:","(Guardrail against importing meaning.)",None,60)]),
 ("7. Present Lesson (Only When the Parable Supplies One)", [
   ("note","(Some parables give a present lesson; others do not.)"),
   ("box","If Jesus gives a present lesson, record it here:",None,None,72),
   ("note","If Jesus does not give one (e.g., Lost Son, Two Debtors, Sheep & Goats), write:"),
   ("quote","Luke/Matthew/Mark gives no explanation, and the study adds none.")]),
 ("8. Notes & Observations", [
   ("box","(For personal study, teaching, or discussion.)",None,None,108)]),
 ]

def E():
    return [
 ("1. Passage Information", [
   ("field","Parable Title:","The Wedding Banquet"),("field","Gospel Passage:","Matthew 22:1–14"),
   ("field","Parallel Passages:","None (Luke 14 is a different parable)")]),
 ("2. Audience & Occasion", [
   ("ans","A. Who is Jesus addressing?",None,["Matthew does not specify at 22:1. The broader day includes:",
      ("b","chief priests and elders (21:23)"),("b","Pharisees (21:45–46)"),("b","Sadducees (22:23)"),("b","the multitude (21:46)")]),
   ("ans","B. What occasion or complaint is He answering?",None,["Matthew records no question before the parable. The parable begins with:",
      ("q","“And Jesus answered and spake unto them again by parables…” (22:1)"),
      "The text does not say what He is answering."])]),
 ("3. The Comparison Jesus Supplies", [
   ("ans","A. What is the comparison?",None,[("q","“The kingdom of heaven is like unto a certain king, which made a marriage for his son.” (22:2)")]),
   ("ans","B. What movement does the story follow?",None,[
      ("n","A king prepares a marriage for his son."),
      ("n","First sending: those bidden “would not come.”"),
      ("n","Second sending: they “made light of it,” went their ways; the remnant slew the servants."),
      ("n","The king sends armies, destroys the murderers, burns their city."),
      ("n","The king sends servants to the highways."),
      ("n","The wedding is furnished with guests, “both bad and good.”"),
      ("n","The king questions a man without a wedding garment."),
      ("n","The man is speechless."),
      ("n","The king commands him to be cast into outer darkness."),
      ("n","Jesus adds: “For many are called, but few are chosen.”")])]),
 ("4. What Jesus Names vs. What He Leaves Unnamed", [
   ("ans","A. Elements Jesus explicitly identifies:",None,[("b",x) for x in
      ["A king","A son","Servants","Those bidden","A dinner","A farm, merchandise","A remnant","Armies","A city","Highways",
       "Guests (bad and good)","A man","A wedding garment","Outer darkness","Weeping and gnashing of teeth","Called and chosen"]]),
   ("ans","B. Elements Jesus does not identify:",None,["Jesus does not identify:"]+[("b",x) for x in
      ["who the king is","who the son is","who the servants are","who those bidden are","who the remnant is","what city is burned",
       "who the highway people are","who the man is","what the garment is","who the called or chosen are"]]),
   ("rule","Rule:","No identities are supplied; none are added.")]),
 ("5. Boundaries of the Parable", [
   ("ans","A. What belongs to this parable only?",None,[("b",x) for x in ["The garment","The burned city","The two sendings","The man cast out","The closing saying"]]),
   ("ans","B. What similar parables must remain separate?",None,[
      ("b","Luke 14 (Great Banquet): one servant, three excuses, no king, no garment"),
      ("b","Matthew 21 (Wicked Tenants): vineyard, son killed"),
      ("b","Matthew 21 (Two Sons): vineyard, command to work"),
      ("b","Matthew 25 (Ten Virgins): bridegroom, lamps, shut door"),
      "No details are merged."])]),
 ("6. The Stated Point", [
   ("ans","A. What point does Jesus make in the text itself?",None,["The comparison shows:"]+[("b",x) for x in
      ["The Kingdom summons is ready.","Refusal has consequences.","The invitation expands outward.","Presumption does not guarantee participation.","Many are called; few are chosen."]]),
   ("ans","B. What the parable does not say:",None,[("b",x) for x in
      ["It does not identify the king, son, guests, garment, or city.","It does not give a doctrine of salvation.","It does not explain the garment.",
       "It does not transfer Kingdom identity to the Body of Christ."]])]),
 ("7. Present Lesson (Only When Supplied)", [
   ("ans","",None,["This parable does allow principled present lessons, because Jesus gives a comparison with moral force.","Principled lessons (not identity transfer):",
      ("b2","Response:","“All things are ready: come” — readiness calls for an answer."),
      ("b2","Weight:","Those bidden “made light of it” — a summons from one with authority is not small."),
      ("b2","No presumption:","A guest present is still examined."),
      ("b2","Humility:","The man is speechless — one may have no answer when called to account.")])]),
 ("8. Notes & Observations", [
   ("ans","",None,[("b",x) for x in ["The son never appears in the story.","The garment is treated as something explainable, but Jesus does not explain it.",
      "The closing saying is added after the story, not part of the narrative.","The parable is told during Jesus’ Kingdom ministry to Israel.",
      "No part of the story is turned into a symbol or doctrine."]])]),
 ]
