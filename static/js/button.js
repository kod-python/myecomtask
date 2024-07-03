$(document).on("click", "#add-cart", function (e) {
  e.preventDefault();

  $.ajax({
    type: "POST",
    url: '{% url "cart_add" %}',
    data: {
      product_id: $("#add-cart").val(),
      csrfmiddlewaretoken: "{{ csrf_token }}",
      action: "post",
    },
    success: function (json) {
      console.log(json);
    },
    error: function (xhr, errmsg, err) {},
  });
});
