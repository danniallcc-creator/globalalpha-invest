class Localization:
  static Map<String, Map<String, String>> values = {
    'zh': {
      'app_title': '跨境出海智库',
      'search_hint': '输入类目查询全球机会...',
      'feature_compass': '消费地图罗盘',
      'feature_thinktank': '国别智库',
      'feature_compliance': '合规查询',
      'feature_aisourcing': 'AI 选品',
      'profit_market': '首选利润国',
      'mass_market': '首选规模国',
      'blue_ocean': '首选蓝海国',
      'generate_report': '一键生成深度报告',
    },
    'en': {
      'app_title': 'Global Intel',
      'search_hint': 'Enter category to find ops...',
      'feature_compass': 'Market Compass',
      'feature_thinktank': 'Country Intel',
      'feature_compliance': 'Compliance',
      'feature_aisourcing': 'AI Sourcing',
      'profit_market': 'Profit Market',
      'mass_market': 'Mass Market',
      'blue_ocean': 'Blue Ocean',
      'generate_report': 'Generate Deep Report',
    }
  };

  static String lang = 'zh';

  static String t(String key) {
    return values[lang]?[key] ?? key;
  }
}
