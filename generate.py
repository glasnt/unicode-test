header = """
<html lang="en">
<head>
  <link rel="stylesheet" href="css/skeleton.css" />
  <link rel="stylesheet" href="css/custom.css" />
  <meta charset="utf-8">
</head>
<body>
  <div class="section">
    <section class="header">
      <h1 class="section-heading">Unicode Infinity Test</h1>
      <h3 id="limit"></h3>
    </section>
  </div>
  <div class="section">
    <div class="container bed-container">
        <div id="bed">
"""

footer = """
</div>
</div>
  </div>
  <div class="section">
    <div class="container">
      <div class="row">
        <hr>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="container">
      <div class="row">
        <p>Add a <code>&#NUMBER;</code> entity in triplicate: entity, entity with VARIATION SELECTOR-15, and VARIATION SELECTOR-16.</p>
      </div>
    </div>
  </div>
"""
fe0e = "&#xFE0E;"
fe0f = "&#xFE0F;"


print(header)
for i in range(127000,130000):
    e = "&#"+str(i)+";";    
    print("<span class='slug'>%s</span>" % "".join([e,e,fe0e,e,fe0f]))
    if i % 10 == 0:
        print("<br>")

print(footer)
