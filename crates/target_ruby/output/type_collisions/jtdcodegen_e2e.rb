# Code generated by jtd-codegen for Ruby v0.1.1

require 'json'
require 'time'

module JTDCodegenE2E

  class RootFooBar
    attr_accessor :x

    def self.from_json_data(data)
      out = RootFooBar.new
      out.x = JTDCodegenE2E::from_json_data(TrueClass, data["x"])
      out
    end

    def to_json_data
      data = {}
      data["x"] = JTDCodegenE2E::to_json_data(x)
      data
    end
  end

  class RootFoo
    attr_accessor :bar

    def self.from_json_data(data)
      out = RootFoo.new
      out.bar = JTDCodegenE2E::from_json_data(RootFooBar, data["bar"])
      out
    end

    def to_json_data
      data = {}
      data["bar"] = JTDCodegenE2E::to_json_data(bar)
      data
    end
  end

  class RootFooBar0
    attr_accessor :x

    def self.from_json_data(data)
      out = RootFooBar0.new
      out.x = JTDCodegenE2E::from_json_data(String, data["x"])
      out
    end

    def to_json_data
      data = {}
      data["x"] = JTDCodegenE2E::to_json_data(x)
      data
    end
  end

  class Root
    attr_accessor :foo
    attr_accessor :foo_bar

    def self.from_json_data(data)
      out = Root.new
      out.foo = JTDCodegenE2E::from_json_data(RootFoo, data["foo"])
      out.foo_bar = JTDCodegenE2E::from_json_data(RootFooBar0, data["foo_bar"])
      out
    end

    def to_json_data
      data = {}
      data["foo"] = JTDCodegenE2E::to_json_data(foo)
      data["foo_bar"] = JTDCodegenE2E::to_json_data(foo_bar)
      data
    end
  end

  private

  def self.from_json_data(type, data)
    if data.nil? || [Object, TrueClass, Integer, Float, String].include?(type)
      data
    elsif type == DateTime
      DateTime.rfc3339(data)
    elsif type.is_a?(Array)
      data.map { |elem| from_json_data(type.first, elem) }
    elsif type.is_a?(Hash)
      data.transform_values { |elem| from_json_data(type.values.first, elem) }
    else
      type.from_json_data(data)
    end
  end

  def self.to_json_data(data)
    if data.nil? || [TrueClass, FalseClass, Integer, Float, String].include?(data.class)
      data
    elsif data.is_a?(DateTime)
      data.rfc3339
    elsif data.is_a?(Array)
      data.map { |elem| to_json_data(elem) }
    elsif data.is_a?(Hash)
      data.transform_values { |elem| to_json_data(elem) }
    else
      data.to_json_data
    end
  end
end
