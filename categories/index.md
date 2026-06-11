---
layout: page
title: 文章分類
permalink: /categories/
---

<div class="row">
{% for category in site.categories %}
  <div class="col-md-4 mb-4">
    <div class="card h-100">
      <div class="card-body text-center">
        <h5 class="card-title">{{ category[0] }}</h5>
        <p class="card-text text-muted">{{ category[1] | size }} 篇文章</p>
        <a href="{{ '/categories/' | append: category[0] | relative_url }}" class="btn btn-outline-primary btn-sm">
          <i class="fas fa-folder-open me-1"></i>瀏覽文章
        </a>
      </div>
    </div>
  </div>
{% endfor %}
</div>