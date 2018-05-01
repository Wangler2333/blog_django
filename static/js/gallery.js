// 绑定删除按钮和切换状态按钮的点击事件，ajax请求删除内容
$(".button_ajax").click(function () {
    var $button = $(this);
    $button.button('loading');
    var name = $button.prop('name');
    var value = $button.prop('value');
    var csrf = $('input[name="csrfmiddlewaretoken"]').prop('value');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: url_gallery,
        data: {'csrfmiddlewaretoken': csrf, 'name': name, 'value': value},
        success: function (result) {
            if (result.resultCode == 200) {
                $.each(result.li_list, function (index, value) {
                    var li_name = '#' + value;
                    $(li_name).remove();
                    window.location.reload();
                });
            }
            if (result.resultCode == 201) {
                var li_name = '#' + result.li_list;
                $(li_name).remove();
                window.location.reload();
            }
            if (result.resultCode == 202) {
                $.each(result.true_list, function (index, value) {
                    $('#' + value).find('.image-show').html('已展示');
                });
                $.each(result.false_list, function (index, value) {
                    $('#' + value).find('.image-show').html('未展示');
                });
            }
            $button.button('reset');
        },
        error: function () {
            $button.button('reset');
        }
    });
});

// 绑定input上传按钮的change事件，ajax请求上传文件
$("#File").change(function () {
    var $button = $("button[name=new]");
    $button.button('loading');
    var csrf = $('input[name="csrfmiddlewaretoken"]').prop('value');
    var formdata = new FormData();
    formdata.append('editormd-image-file', $('#File').get(0).files[0]);
    formdata.append('csrfmiddlewaretoken', csrf);
    $.ajax({
        type: "POST",
        url: url_upload,
        contentType: false,
        data: formdata,
        processData: false,
        success: function (result) {
            if (result.success == 1) {
                window.location.reload();
            }
            if (result.success == 0) {
                alert(result.message);
            }
            $button.button('reset');
        },
        error: function () {
            alert('传输异常');
            $button.button('reset');
        }
    });
});

// 绑定新增按钮，模拟点击input上传按钮
$("button[name=new]").click(function clp() {
    $("#File").click();

});

// 绑定设置按钮，更改弹出框id并显示
$("button[name=set]").click(function () {
    var val = $(this).prop('value');
    var modal_div = $('.doc-modal-null');
    modal_div.prop('id', 'doc-modal-' + val);
    $('#modal-image-id').prop('value', '' + val);
    $('#doc-modal-' + val).modal();
});

// 绑定弹出框确认按钮，ajax请求
$('#modal-form-confirm').click(function () {
    var form_data = $('#modal-form').serialize();
    var csrf = $('input[name="csrfmiddlewaretoken"]').prop('value');
    var json_data = form_data + "&csrfmiddlewaretoken=" + csrf;
    var image_id = $('#modal-image-id').prop('value');
    var $button = $("#set-" + image_id);
    $button.button('loading');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: url_gallery,
        data: json_data,
        success: function (result) {
            if (result.resultCode == 200) {
                var image = $('#' + result.id);
                if (result.title) {
                    image.find('.image-title').html(result.title);
                }
                if (result.show == 'on') {
                    image.find('.image-show').html('已展示')
                } else {
                    image.find('.image-show').html('未展示')
                }
            }
            if (result.resultCode == 201) {
            }
            $button.button('reset');
        },
        error: function () {
            alert("设置异常");
            $button.button('reset');
        }
    });
});

// 文章的全选和全不选，并记录已选的value
$('.article_form_title').find(':checkbox').change(function () {
    var select_check = '';
    // 获取全选的checkbox的选中状态
    var is_checked = $(this).prop('checked');
    // 遍历商品的对应的checkbox，设置这些checkbox的选中状态和全选的checkbox保持一致
    $('.article_list_body').find(':checkbox').each(function () {
        $(this).prop('checked', is_checked);
    });
    $('.article_list_body').find(':checked').each(function () {
        select_check = $(this).prop('name') + ',' + select_check
    });
    $('button[name="delete_select"]').prop('value', select_check);
    $('button[name="set_select"]').prop('value', select_check);
});

// 文章对应的checkbox状态发生改变时，设置全选checkbox的状态，并记录已选的value
$('.article_list_body').find(':checkbox').change(function () {
    var select_check = '';
    // 获取页面上所有商品的数目
    var all = $('.article_list_body').find(':checkbox');
    // 获取页面上被选中的商品的数目
    var checked = $('.article_list_body').find(':checked');
    var is_checked = true;
    if (checked.length < all.length) {
        is_checked = false;
    }
    checked.each(function () {
        select_check = $(this).prop('name') + ',' + select_check
    });
    $('button[name="delete_select"]').prop('value', select_check);
    $('button[name="set_select"]').prop('value', select_check);
    $('.article_form_title').find(':checkbox').prop('checked', is_checked);
});
