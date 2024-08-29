const cardMore = document.getElementById('more')
const btnMore = document.getElementById('btn_more')
const quitCard = document.getElementById('quitCard')
const likeBtnList = document.querySelectorAll('.like')
const retweetBtnList = document.querySelectorAll('.retweet')
const bookmarkBtnList = document.querySelectorAll('.bookmark')
console.log(retweetBtnList)

// Afficher l'interface + dans l'acceuil

btnMore.addEventListener('click',()=>{
    cardMore.classList.toggle('hidden')
})
quitCard.addEventListener('click',()=>{
    cardMore.classList.toggle('hidden')
})




// Rendre les onglets du profile interactif
const newTweetBtn = document.querySelector('#new-tweet')
newTweetBtn.addEventListener('click', ()=>{
    console.log('Le bouton a bien été cliqué')
})



function setReplace(img, actived, unactived){
    if(img.attributes.src.value==unactived){
        img.attributes.src.value=actived
    }else{
        img.attributes.src.value=unactived
    }
}
const LIKED = "../../static/img/liked_icon.svg"
const UNLIKED = "../../static/img/unliked_icon.svg"
// Rendre les like interactifs
likeBtnList.forEach((img)=>{
    img.addEventListener('click',()=>{
        setReplace(img, LIKED, UNLIKED)
    })
})

const UNRETWEETED = "../../static/img/icons8-retweet-48.png"
const RETWEETED = "../../static/img/icons8-retweeted-48.png"
// Rendre les retweets interactifs
retweetBtnList.forEach((retweet)=>{
    retweet.addEventListener('click',()=>{
        setReplace(retweet, RETWEETED, UNRETWEETED)
    })
})

const UNBOOKMARKED = "../../static/img/bookmark_icon.svg"
const BOOKMARKED = "../../static/img/icons8-bookmark-30.png"
// Rendre les retweets interactifs
bookmarkBtnList.forEach((bookmark)=>{
    bookmark.addEventListener('click',()=>{
        setReplace(bookmark, BOOKMARKED, UNBOOKMARKED)
    })
})


// Rendre les onglets du profile interactif
const navItem = document.querySelectorAll('.nav-item p')
let actived = document.querySelector('#tweets')
//actived.classList.add('active')
navItem.forEach( (item)=>{
    item.addEventListener('click', ()=>{
        item.classList.toggle('active')
        actived.classList.remove('active')
        actived = item
    })
})


// Rendre le bouton de commentaire dynamique
const commentBtn = document.querySelector('#commentDetailsBtn')
const commentInput = document.querySelector('#commentDetailsInput')

commentInput.addEventListener('click', (input)=>{
    if(input.target){
        input.classList.remove('text-grey')
        input.classList.toggle('text-white')
    }
})