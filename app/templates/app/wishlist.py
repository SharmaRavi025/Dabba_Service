{% extends 'app/base.html' %}
{% load static %}
{% block title %}Update Address{% endblock title %}
{% block main-content %}

<div class="container my-5">
  <div class="row">
    <div class="col-sm-8">
      <div class="row">
        {% for prod in product %}
          <div class="col-sm-4 text-center mb-4 hover-shadow">
            <a href="{% url 'product-detail' prod.product.id %}" class="btn">
              <div>
                <img src="{{prod.product.product_image.url}}" width="300px" height="200px" />
                <div class="fw-bold">{{prod.product.title}}</div>
                <div class="fw-bold text-danger">
                    RS.{{prod.product.discounted_price}}/-
                    <small class="fw-light text-decoration-line-through">{{prod.product.selling_price}}</small>
                </div>
              </div>
            </a>
          </div>
        {% endfor %}
      </div>
    </div>    
  </div>
</div>

{% endblock main-content %} 