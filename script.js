var awesome = `
You are on the right way, but now, more things need to be done.

7573652070617373776f726420746f20646563727970742e2043697068657220656e6372797074656420696e205243342c2073686f776e20696e204261736536342e

`;

const colleges = [
    '条目sd1', '条awf目2', '条sdg目3', '条目4',
    '条sdd目1', '条目2', '条目dsg3', '条目4',
    '条sgsdgsg目1', '条fas目2', '条safsa目3', '条目4',
    '条edsg目1', '条fasf目2', '条目3', '条目4',
    '条目1', '条sd目2', '条sdgdgs目3', '条目4',
]

function sleep(ms) {
    return new Promise(function (resolve, reject) { setTimeout(resolve, ms) })
}

function randInt(a, b) {
    return Math.floor(Math.random() * (b - a + 1) + a);
}

function addAllColleges() {
    let html = ""
    for (let i of colleges) {
        let color = `rgba(${randInt(220, 255)},${randInt(220, 255)},${randInt(220, 255)},0.8);`;
        html += `
        <div 
            class="item" 
            style="background-color: ${color}">
            ${i}
        </div>`;
    }
    $("#content").html(html);
}

async function getRandomSchool() {
    let i = randInt(0, colleges.length - 1);
    let name = colleges[i];
    // hide
    $("#content").css("opacity", 0);
    await sleep(600);
    // generate dom
    $("#content").html(`
    <div
        class="big-item"
        style="background: rgba(${randInt(220, 255)},${randInt(220, 255)},${randInt(220, 255)}, 0.5);">
        ${name}
    </div>
    `);
    // show
    $("#content").css("opacity", 1);
}


$(document).ready(function () {
    addAllColleges();
});