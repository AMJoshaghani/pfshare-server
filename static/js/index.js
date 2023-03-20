function $(selector, GetAll = false) {
    return GetAll ? document.querySelectorAll(selector) : document.querySelector(selector);
}

function getPath(el) {
    var stack = [];
    while (el.parentNode != null) {
        var sibCount = 0;
        var sibIndex = 0;
        for (var i = 0; i < el.parentNode.childNodes.length; i++) {
            var sib = el.parentNode.childNodes[i];
            if (sib.nodeName == el.nodeName) {
                if (sib === el) {
                    sibIndex = sibCount;
                    break;
                }
                sibCount++;
            }
        }
        if (el.hasAttribute('id') && el.id != '') {
            stack.unshift(el.nodeName.toLowerCase() + '#' + el.id);
        } else if (sibCount > 0) {
            stack.unshift(el.nodeName.toLowerCase() + ':nth-child(' + (sibIndex + 1) + ')');
        } else {
            stack.unshift(el.nodeName.toLowerCase());
        }
        el = el.parentNode;
    }
    return stack.slice(1);
    // https://gist.github.com/karlgroves/7544592
}

function showPopUp(element) {
    let offsetRight = window.innerWidth - element.getBoundingClientRect().right;
    let offsetBottom = window.innerHeight - element.getBoundingClientRect().bottom;
    ////
    let popUp = $(getPath(element).join(" > ").toString() + " .pop-up");
    popUp.style.display = "table";
    let popUpWidth = popUp.offsetWidth;
    let popUpHeight = popUp.offsetHeight;
    ////
    if ((offsetRight - popUpWidth) < 100) {
        popUp.style.right = ((popUpWidth * 25) / 100).toString() + "px"; // 25% of element width
    }
    if ((offsetBottom - popUpHeight) < 100) {
        popUp.style.bottom = ((popUpHeight * 25) / 100).toString() + "px"; // 25% of element height
    }
}

function hidePopUp(element) {
    let popUp = $(getPath(element).join(" > ").toString() + " .pop-up");
    popUp.style.display = 'none';
}

function addListeners(xhr, handleEvent) {
    xhr.addEventListener('loadstart', handleEvent);
    xhr.addEventListener('load', handleEvent);
    xhr.addEventListener('loadend', handleEvent);
    xhr.addEventListener('progress', handleEvent);
    xhr.addEventListener('error', handleEvent);
    xhr.addEventListener('abort', handleEvent);
}