import json

with open("history.json") as inFile:
    history = json.load(inFile)

def timePlacement(begin, end):
    top = 0
    bot = 0

    if (begin < -500):
        top = -4000 - begin
        top /= 5
    elif (begin >= -500 and begin < 500):
        top = -500 - begin
        top -= 700
    elif (begin >= 500 and begin < 1000):
        top = 500 - begin
        top -= 1700
    elif (begin >= 1000 and begin < 1500):
        top = 1000 - begin
        top -= 2200
    elif (begin >= 1500 and begin < 1800):
        top = 1500 - begin
        top /= 0.5
        top -= 2700
    elif (begin >= 1800 and begin < 1915):
        top = 1800 - begin
        top /= 0.25
        top -= 3300
    elif (begin >= 1915):
        top = 1915 - begin
        top /= 0.15
        top -= 3760

    # print("top is    ", int(-top))

    if (end < -500):
        bot = -4000 - end
        bot /= 5
    elif (end >= -500 and end < 500):
        bot = -500 - end
        bot -= 700
    elif (end >= 500 and end < 1000):
        bot = 500 - end
        bot -= 1700
    elif (end >= 1000 and end < 1500):
        bot = 1000 - end
        bot -= 2200
    elif (end >= 1500 and end < 1800):
        bot = 1500 - end
        bot /= 0.5
        bot -= 2700
    elif (end >= 1800 and end < 1915):
        bot = 1800 - end
        bot /= 0.25
        bot -= 3300
    elif (end >= 1915):
        bot = 1915 - end
        bot /= 0.15
        bot -= 3760

    # print("height is ", int(-bot - -top))

    return int(-top), int(-bot - -top)

# colors = ["coral", "darkturquoise", "dodgerblue", "floralwhite", "plum", "chocolate", "lavender", "goldenrod", "MediumVioletRed", "DeepPink", "firebrick", "palegreen", "seagreen", "lightslategray", "honeydew", "lightsteelblue", "springgreen", "wheat", "slateblue", "orchid", "darkorange", "lightsteelblue", "mediumaquamarine"]
colors = ["#e4e4e4"]
def colorGenerator(name):
    value = 0
    for l in name:
        value += ord(l)
    
    return colors[value % len(colors)]

with open("generated.html", "w") as outFile:

    outFile.write("""
<html>
<head>
    <title>History Timeline</title>
    <link href="main.css" type="text/css" rel="stylesheet"/>
</head>
<body>
    <div id="year-display">0000 CE</div>
    <div id="container">
        <div class="region-title">Year</div>
        <div class="region-title">Africa</div>
        <div class="region-title">Asia</div>
        <div class="region-title">Europe</div>
        <div class="region-title">Middle East</div>
        <div class="region-title">Southeast Asia</div>
        <div class="region-title">North America</div>
        <div class="region-title">South America</div>
        <div class="region-title">Oceania</div>

        <div class="region-content">
            <div class="dynasty" style="top: 0px; height: 700px; background: plum; opacity: 0.95;">
                <p class="dynasty-begin">4000 BCE</p>
                <p class="dynasty-content">Early Complex Societies (Lines = 500 Years)</p>
                <p class="dynasty-end">500 BCE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
                <hr class="timeline-marker" style="top: 500px">
                <hr class="timeline-marker" style="top: 600px">
            </div>
            <div class="dynasty" style="top: 700px; height: 1000px; background: crimson; opacity: 0.95;">
                <p class="dynasty-begin">500 BCE</p>
                <p class="dynasty-content">Classical Societies (Lines = 100 Years)</p>
                <p class="dynasty-end">500 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
                <hr class="timeline-marker" style="top: 500px">
                <hr class="timeline-marker" style="top: 600px">
                <hr class="timeline-marker" style="top: 700px">
                <hr class="timeline-marker" style="top: 800px">
                <hr class="timeline-marker" style="top: 900px">
            </div>
            <div class="dynasty" style="top: 1700px; height: 500px; background: peru; opacity: 0.95;">
                <p class="dynasty-begin">500 CE</p>
                <p class="dynasty-content">Post Classical Societies (Lines = 100 Years)</p>
                <p class="dynasty-end">1000 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
            </div>
            <div class="dynasty" style="top: 2200px; height: 500px; background: wheat; opacity: 0.95;">
                <p class="dynasty-begin">1000 CE</p>
                <p class="dynasty-content">Cross Cultural Interaction (Lines = 100 Years)</p>
                <p class="dynasty-end">1500 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
            </div>
            <div class="dynasty" style="top: 2700px; height: 600px; background: mediumaquamarine; opacity: 0.95;">
                <p class="dynasty-begin">1500 CE</p>
                <p class="dynasty-content">Global Interdependence (Lines = 50 Years)</p>
                <p class="dynasty-end">1800 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
                <hr class="timeline-marker" style="top: 500px">
                <hr class="timeline-marker" style="top: 600px">
                <hr class="timeline-marker" style="top: 700px">
            </div>
            <div class="dynasty" style="top: 3300px; height: 460px; background: DarkCyan; opacity: 0.95;">
                <p class="dynasty-begin">1800 CE</p>
                <p class="dynasty-content">Industry and Imperialism (Lines = 25 Years)</p>
                <p class="dynasty-end">1915 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
            </div>
            <div class="dynasty" style="top: 3760px; height: 500px; background: CornflowerBlue; opacity: 0.95;">
                <p class="dynasty-begin">1915 CE</p>
                <p class="dynasty-content">The Contemporary World (Lines = 15 Years)</p>
                <p class="dynasty-end">1990 CE</p>
                <hr class="timeline-marker" style="top: 100px">
                <hr class="timeline-marker" style="top: 200px">
                <hr class="timeline-marker" style="top: 300px">
                <hr class="timeline-marker" style="top: 400px">
            </div>
        </div>
    """)

    for region in history:
        outFile.write("""<div class="region-content" id="{0}">\n""".format(region))
        for dynasty in history[region]:
            pixLocate = timePlacement(history[region][dynasty]["begin"], history[region][dynasty]["end"])
            side = ""
            if (history[region][dynasty]["side"] == 1):
                side = "right: calc(50% + 2px); "
            elif (history[region][dynasty]["side"] == 2):
                side = "left: calc(50% + 2px); "
            
            beginString = ''
            endString = ''
            if (abs(history[region][dynasty]["begin"] - history[region][dynasty]["end"]) > 30) and dynasty != "New Babylonians":
                if (history[region][dynasty]["begin"] > 0):
                    beginString = '<p class="dynasty-begin">' + str(abs(history[region][dynasty]["begin"])) + " CE" + "</p>"
                else:
                    beginString = '<p class="dynasty-begin">' + str(abs(history[region][dynasty]["begin"])) + " BCE" + "</p>"
                if (history[region][dynasty]["end"] > 0):
                    endString = '<p class="dynasty-end">' + str(abs(history[region][dynasty]["end"])) + " CE" + "</p>"
                else:
                    endString = '<p class="dynasty-end">' + str(abs(history[region][dynasty]["end"])) + " BCE" + "</p>"

            outFile.write(
"""
    <div class="dynasty" style="top: {0}px; height: {1}px; {2}background: linear-gradient(to bottom, rgba(200, 200, 200, 0.6), {3});">
        {4}
        <p class="dynasty-content">{5}</p>
        {6}
        <span class="dynasty-info">
            {5}
            <p>{7}</p>
        </span>
    </div>
""".format(pixLocate[0], pixLocate[1], side, colorGenerator(dynasty), beginString, dynasty, endString, history[region][dynasty]["desc"]))

        outFile.write("\n</div>")
    outFile.write(
"""

<script>

    var element = document.getElementById('container');
    var box = document.getElementById('year-display');
    var year = 0;

    var drawLines = function(event) {
        var y = event.pageY;
        var hrLine = element.querySelector('.hrLine');

        if (!hrLine) {
            hrLine = document.createElement('div');
            hrLine.style.height = "4px";
            hrLine.style.zIndex = "-1";
            hrLine.classList.add('hrLine');
            hrLine.style.width = '100%';
            element.appendChild(hrLine);
        }
        hrLine.style.transform = 'translate(0px, ' + y + 'px)';
        // console.log(y);

        if (y >= 30 && y < 730) {
            box.style.display = "flex";
            year = (y-30) * 5;
            year -= 4000;
        } else if (y >= 730 && y < 1730) {
            box.style.display = "flex";
            year = (y-30);
            year -= 1200;
        } else if (y >= 1730 && y < 2230) {
            box.style.display = "flex";
            year = (y-30);
            year -= 1200;
        } else if (y >= 2230 && y < 2730) {
            box.style.display = "flex";
            year = (y-30);
            year -= 1200;
        } else if (y >= 2730 && y < 3330) {
            box.style.display = "flex";
            year = Math.round((y-30) * 0.5);
            year += 150;
        } else if (y >= 3330 && y < 3790) {
            box.style.display = "flex";
            year = Math.round((y-30) * 0.25);
            year += 975;
        } else if (y >= 3790 && y < 4290) {
            box.style.display = "flex";
            year = Math.round((y-30) * 0.15);
            year += 1350;
        } else {
            box.style.display = "none";
        }

        if (year < 0) {
            box.innerHTML = -year + " BCE";
        } else {
            box.innerHTML = year + " CE";
        }
    }

    element.addEventListener('mousemove', function(event) { drawLines(event); });
    element.addEventListener('mouseout', function(event) { drawLines(event); });

    var el = document.getElementByClass("dynasty-info");
    do {
        var styles = window.getComputedStyle(el);
        console.log(styles.zIndex, el);
    } while(el.parentElement && (el = el.parentElement));

</script>
</body>
</html>
""")
