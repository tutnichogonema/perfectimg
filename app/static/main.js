$(window).load(function() {
var images = $('img');
for (i = 0; i < images.length; i++) {
    if (0 < images[i].clientWidth && images[i].clientWidth < 200) {
        images[i].style.width = "300px";
    } else if (200 <= images[i].clientWidth && images[i].clientWidth < 400) {
        images[i].style.width = "300px";
    } else if (400 <= images[i].clientWidth) {
        images[i].style.width = "300px";
    } else {
        console.log("bida!");
    }
}

var container = document.querySelector('#container');
var pckry = new Packery( container, {
  itemSelector: '.item',
  gutter: 10
});
$container.infinitescroll({
            navSelector:'div.paginate',
            nextSelector:'div.paginate a.next',
            itemSelector:'article.item',
            loading:{
                finishedMsg:'No more pages to load.'
            }
        },
        function(newElements) {
            $(newElements).imagesLoaded(function(){
                $container.packery('appended', newElements);
            });
        });
})
jQuery(document).ready(function() {
    jQuery("img.lazy").lazy();
});
