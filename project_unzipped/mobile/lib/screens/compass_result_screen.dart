import 'dart:ui';
import 'package:flutter/material.dart';

class CompassResultScreen extends StatelessWidget {
  final String category;

  CompassResultScreen({required this.category});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: Text(category),
        actions: [
          IconButton(icon: Icon(Icons.favorite_border), onPressed: () {}),
          IconButton(icon: Icon(Icons.ios_share), onPressed: () {}),
        ],
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Color(0xFF020B18), Color(0xFF0D1B2A)],
          ),
        ),
        child: SingleChildScrollView(
          padding: EdgeInsets.fromLTRB(20, kToolbarHeight + 40, 20, 20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildHeader(),
              SizedBox(height: 24),
              _buildModernResultCard('首选利润国', '德国 / 澳大利亚', '高购买力 & 电费补贴政策', Colors.green),
              _buildModernResultCard('首选规模国', '美国', '成熟电商基建 & 露营文化', Colors.blueAccent),
              _buildModernResultCard('首选蓝海国', '巴西 / 印尼', '人口年轻 & 能源缺口爆发', Colors.purpleAccent),
              SizedBox(height: 32),
              _buildInsightSection(),
              SizedBox(height: 32),
              _buildGenerateButton(context),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('市场决策矩阵', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
        SizedBox(height: 8),
        Text('基于 GDP、增长率与行业基建深度分析', style: TextStyle(color: Colors.white38)),
      ],
    );
  }

  Widget _buildModernResultCard(String title, String countries, String reason, Color color) {
    return Container(
      margin: EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.03),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: color.withOpacity(0.2)),
      ),
      clipBehavior: Clip.antiAlias,
      child: Stack(
        children: [
          Positioned(
            right: -20,
            top: -20,
            child: Icon(Icons.language, size: 100, color: color.withOpacity(0.05)),
          ),
          Padding(
            padding: EdgeInsets.all(24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Container(
                      width: 12,
                      height: 12,
                      decoration: BoxDecoration(color: color, shape: BoxShape.circle),
                    ),
                    SizedBox(width: 10),
                    Text(title, style: TextStyle(color: color, fontWeight: FontWeight.bold, fontSize: 14, letterSpacing: 1.2)),
                  ],
                ),
                SizedBox(height: 16),
                Text(countries, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, letterSpacing: -0.5)),
                SizedBox(height: 8),
                Text(reason, style: TextStyle(color: Colors.white54, fontSize: 14)),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInsightSection() {
    return Container(
      padding: EdgeInsets.all(24),
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [Colors.blue.withOpacity(0.1), Colors.purple.withOpacity(0.1)]),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.white.withOpacity(0.05)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.auto_awesome, color: Colors.blueAccent, size: 20),
              SizedBox(width: 10),
              Text('专家行动策略', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            ],
          ),
          SizedBox(height: 16),
          Text(
            '针对德国市场，建议主打‘工业级稳定性’及‘多机并网’功能。由于当地 EEG 法案支持，用户对能够‘反向送电’获利的系统有极高溢价空间。',
            style: TextStyle(color: Colors.white70, height: 1.6, fontSize: 15),
          ),
        ],
      ),
    );
  }

  Widget _buildGenerateButton(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 60,
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [Colors.blueAccent, Colors.blue]),
        borderRadius: BorderRadius.circular(18),
        boxShadow: [BoxShadow(color: Colors.blueAccent.withOpacity(0.3), blurRadius: 20, offset: Offset(0, 10))],
      ),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          primary: Colors.transparent,
          shadowColor: Colors.transparent,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
        ),
        onPressed: () {
          ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('报告已开始生成，请在个人中心查看')));
        },
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.description_outlined),
            SizedBox(width: 12),
            Text('一键生成 4K 深度分析报告', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
