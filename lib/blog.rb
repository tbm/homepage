
def create_blog_index

    Dir.glob("content/blog/**/*/").each do |dir|
        dir.gsub!("content", "")
        lastmod = sorted_articles.select { |a| a.identifier.start_with?(dir) }.map { |a| a[:created_at] }.max
        @items << Nanoc3::Item.new(
        "",
        { :extension => 'erb', :mtime => lastmod, :kind => "blog-index", :title => "Blog of Martin Michlmayr" },
        dir,
        )
    end

end

