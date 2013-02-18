module Nanoc3::Filters

  # Remove lines that only consist of whitespace - they are introduced
  # by ERB commands.
  class RemoveLinesWithOnlyWhitespace < Nanoc3::Filter

    identifiers :remove_lines_with_only_whitespace

    def run(content, arguments={})
      content.gsub(/\n\s+\n/, "\n")
    end

  end

end

