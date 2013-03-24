---
title: Blog of Martin Michlmayr
nav: Blog
description: The blog of Martin Michlmayr
keywords: [Martin Michlmayr, journal, blog]
---

<% sorted_articles.each do |post| %>
<%= render 'blog-inline', { :post => post } %>
<% end %>

