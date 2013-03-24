---
title: Blog archive of Martin Michlmayr
description: The blog archive of Martin Michlmayr
keywords: [Martin Michlmayr, journal, blog, archive]
---

<ul>
<% sorted_articles.each do |post| %>
<li><%= link_to post[:title], post.path %> (<%= post[:created_at].strftime "%Y-%m-%d" %>)</li>
<% end %>
</ul>

