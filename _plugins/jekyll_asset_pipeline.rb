require 'japr'

module JAPR
    class LessConverter < JAPR::Converter
      require 'less'

      def self.filetype
        '.less'
      end

      def convert
        return Less::Parser.new.parse(@content).to_css
      end
    end
  end
