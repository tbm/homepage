---
title: Summaries of PhD research
keywords: [Martin Michlmayr, PhD, research, blog]
---

<% sorted_articles.select { |a| a.identifier.start_with?("/blog/phd/") }.reverse.each do |post| %>
<%= render 'blog-inline', { :post => post } %>
<% end %>

