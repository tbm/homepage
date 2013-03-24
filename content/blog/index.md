---
title: Blog of Martin Michlmayr
nav: Blog
description: The blog of Martin Michlmayr
keywords: [Martin Michlmayr, journal, blog]
---

<% max = 10 %>

<% sorted_articles.first(max).each do |post| %>
<%= render 'blog-inline', { :post => post } %>
<% end %>

<% if sorted_articles.length > max %>
You can find older blog articles in my <%= link_to "blog archive", @items["/blog/archive/"] %>.
<% end %>

