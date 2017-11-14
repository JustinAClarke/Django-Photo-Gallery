


function photo_list_hash() {
    var list = document.getElementsByClassName("photo"),
    hash = window.location.hash.substr(1);
    for(i=0;i<list.length; i++){
        var data_href = list[i].getAttribute("data-href");
        if(data_href.includes(hash)){
            list[i].style = "display:block;";
        }
        else{
            list[i].style = "display:none;";
        }
    }
}

function nav_active(){
    var list = document.getElementsByClassName("nav"),
    path = window.location.pathname;
    for(i=0;i<list.length; i++){
        var href = list[i].getAttribute("href");
        if(href == path){
            list[i].id = "path_active";
        }
        
    }
    
    
}

nav_active();
