const search = (id,valueId) =>{
    searchIndex=0;
    searchElement = document.getElementById(valueId).value;
    console.log("input:-",searchElement);
    ul = document.getElementById(id);
    allLi = ul.getElementsByTagName("LI");
    console.log("ul before searching:-",ul);
    for(i=0;i<(allLi.length);i++){
        if((allLi[i].innerText.toLowerCase()).startsWith(searchElement.toLowerCase())){
            allLi[searchIndex].parentNode.insertBefore(allLi[i], allLi[searchIndex]);
            searchIndex+=1;
        }
    }
    for(j=searchIndex; j<(allLi.length);j++){
        if((allLi[j].innerText.toLowerCase()).includes(searchElement.toLowerCase())){
            allLi[searchIndex].parentNode.insertBefore(allLi[j], allLi[searchIndex]);
            searchIndex+=1;
        }
    }
}