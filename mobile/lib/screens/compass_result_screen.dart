import 'package:flutter/material.dart';

class CompassResultScreen extends StatelessWidget {
  final String category;

  CompassResultScreen({required this.category});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('$category - 罗盘分析'),
        actions: [
          IconButton(icon: Icon(Icons.favorite_border), onPressed: () {}),
          IconButton(icon: Icon(Icons.share), onPressed: () {}),
        ],
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildResultCard('首选利润国', '德国 / 澳大利亚', '高支付能力、高能效需求。', Colors.green),
            _buildResultCard('首选规模国', '美国', '海量市场基数、成熟电商物流。', Colors.blue),
            _buildResultCard('首选蓝海国', '巴西 / 印尼', '人口红利显著、中方贸易高增速。', Colors.purple),
            SizedBox(height: 20),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton.icon(
                    icon: Icon(Icons.picture_as_pdf),
                    label: Text('一键生成报告'),
                    style: ElevatedButton.styleFrom(primary: Colors.blueAccent, padding: EdgeInsets.symmetric(vertical: 12)),
                    onPressed: () {
                      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('正在生成 $category 深度报告 PDF...')));
                      // In a real app, call ApiService.fetchReport(category) and use url_launcher to open result['download_url']
                    },
                  ),
                ),
              ],
            ),
            SizedBox(height: 20),
            Text('建议方案', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            Card(
              margin: EdgeInsets.symmetric(vertical: 10),
              color: Colors.white10,
              child: Padding(
                padding: EdgeInsets.all(16),
                child: Text('由于当地政策补贴（如德国 EEG 法案），建议优先推广集成“反向并网”功能的储能设备。', style: TextStyle(color: Colors.white70)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildResultCard(String title, String countries, String reason, Color color) {
    return Card(
      margin: EdgeInsets.only(bottom: 16),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
      child: Container(
        padding: EdgeInsets.all(16),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(15),
          border: Border.all(color: color.withOpacity(0.5)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(children: [Icon(Icons.stars, color: color), SizedBox(width: 8), Text(title, style: TextStyle(color: color, fontWeight: FontWeight.bold))]),
            SizedBox(height: 8),
            Text(countries, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            Text(reason, style: TextStyle(color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}
