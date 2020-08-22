function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total - 1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

function deleteForm(selector, type) {
    var total = parseInt($('#id_' + type + '-TOTAL_FORMS').val());
    if (total > 2){
        var delElement = $(selector);
        delElement.remove();
        total--;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
    }
    else {
        alert('Minimum two options are required');
    }
}