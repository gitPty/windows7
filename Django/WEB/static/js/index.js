/**
 * Created by Administrator on 2019/6/18.
 */

 $(function() {

     $('.top').hide();      //先将.top隐藏

     //当滚动条的垂直位置距顶部100像素一下时，跳转链接出现，否则消失
     $(window).scroll(function() {
         if ($(window).scrollTop() > 100) {
             $('.top').fadeIn(1000);
         } else {
             $(".top").fadeOut(1000);
         }
     });

     $(".top").click(function () {
          $(window).scrollTop(0)        //返回顶部
     })
 });

//表格正反选
function selectall_one() {
    // 查找 selectall_one 的后代checkbox, 通过prop方法设置属性为true
    $(".selectall_one :checkbox").prop('checked', true)
}
function cacel_one() {
    $(".selectall_one :checkbox").prop('checked', false)
}

//表格正反选
function selectall_two() {
    $(".selectall_two :checkbox").prop('checked', true)
}
function cacel_two() {
    $(".selectall_two :checkbox").prop('checked', false)
}

//禁止F5重新提交数据
if ( window.history.replaceState ) {
                window.history.replaceState( null, null, window.location.href );
            }

//禁止F5刷新
// window.onload = function() {
//     document.onkeydown = function (e) {
//         if (e.keyCode === 116) {
//             return false;
//         }
//     };
// };



