import 'dart:ui';
import 'package:flutter/material.dart';
import 'compass_result_screen.dart';
import 'compliance_detail_screen.dart';
import 'profile_screen.dart';
import 'chat_screen.dart';
import '../services/api_service.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        leading: IconButton(
          icon: Container(
            padding: EdgeInsets.all(8),
            decoration: BoxDecoration(color: Colors.white10, shape: BoxShape.circle),
            child: Icon(Icons.person_outline, size: 20),
          ),
          onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (c) => ProfileScreen())),
        ),
        title: Text('CROSS-BORDER'),
        actions: [
          IconButton(
            icon: Icon(Icons.auto_awesome, color: Colors.blueAccent),
            onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (c) => ChatScreen())),
          ),
        ],
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF020B18), Color(0xFF0A192F), Color(0xFF020B18)],
          ),
        ),
        child: SingleChildScrollView(
          child: Column(
            children: [
              SizedBox(height: kToolbarHeight + 40),
              _buildMarketTickerSection(),
              _buildHeroSection(),
              _buildFeatureGrid(context),
              _buildRecentTrendsSection(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildMarketTickerSection() {
    return FutureBuilder<Map<String, dynamic>>(
      future: ApiService.fetchMarketData(),
      builder: (context, snapshot) {
        String gold = snapshot.hasData ? "\$${snapshot.data!['gold']['price']}" : "---";
        String usd = snapshot.hasData ? "${snapshot.data!['forex'][0]['rate'].toStringAsFixed(2)}" : "---";
        
        return Container(
          margin: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          padding: EdgeInsets.symmetric(vertical: 12, horizontal: 20),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.05),
            borderRadius: BorderRadius.circular(15),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              _tickerItem('伦敦金', gold, Colors.amber),
              _tickerItem('USD/CNY', usd, Colors.blueAccent),
            ],
          ),
        );
      },
    );
  }

  Widget _tickerItem(String label, String value, Color color) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: TextStyle(color: Colors.white54, fontSize: 10)),
        Text(value, style: TextStyle(color: color, fontSize: 16, fontWeight: FontWeight.bold, letterSpacing: 1)),
      ],
    );
  }

  Widget _buildHeroSection() {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('全球智库', style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, letterSpacing: -1)),
          Text('助力中国商家出海决策', style: TextStyle(color: Colors.white38, fontSize: 16)),
          SizedBox(height: 24),
          _buildGlassSearchBar(),
        ],
      ),
    );
  }

  Widget _buildGlassSearchBar() {
    return ClipRRect(
      borderRadius: BorderRadius.circular(30),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 20, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.1),
            borderRadius: BorderRadius.circular(30),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
          ),
          child: TextField(
            decoration: InputDecoration(
              hintText: '输入类目查询全球机会...',
              hintStyle: TextStyle(color: Colors.white24),
              border: InputBorder.none,
              icon: Icon(Icons.search, color: Colors.blueAccent),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildFeatureGrid(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 16),
      child: GridView.count(
        shrinkWrap: true,
        physics: NeverScrollableScrollPhysics(),
        crossAxisCount: 2,
        mainAxisSpacing: 16,
        crossAxisSpacing: 16,
        childAspectRatio: 1.1,
        children: [
          _glassFeatureCard(context, '消费地图罗盘', Icons.explore, Colors.blue, () {
            Navigator.push(context, MaterialPageRoute(builder: (c) => CompassResultScreen(category: "户外储能")));
          }),
          _glassFeatureCard(context, '国别智库', Icons.language, Colors.green, () {}),
          _glassFeatureCard(context, '合规查询', Icons.verified_user_outlined, Colors.orange, () {
            Navigator.push(context, MaterialPageRoute(builder: (c) => ComplianceDetailScreen()));
          }),
          _glassFeatureCard(context, 'AI 选品', Icons.auto_graph, Colors.purple, () {
             Navigator.push(context, MaterialPageRoute(builder: (c) => ChatScreen()));
          }),
        ],
      ),
    );
  }

  Widget _glassFeatureCard(BuildContext context, String title, IconData icon, Color color, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
          child: Container(
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.05),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: Colors.white.withOpacity(0.05)),
            ),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: EdgeInsets.all(12),
                  decoration: BoxDecoration(color: color.withOpacity(0.1), shape: BoxShape.circle),
                  child: Icon(icon, color: color, size: 28),
                ),
                SizedBox(height: 12),
                Text(title, style: TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildRecentTrendsSection() {
    return Container(
      padding: EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('实时选品趋势', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              Text('查看全部', style: TextStyle(color: Colors.blueAccent, fontSize: 14)),
            ],
          ),
          SizedBox(height: 16),
          _trendItem('便携储能电池', '德国站搜索量飙升 120%', 'AMZ', Colors.green),
          _trendItem('智能割草机器人', '北美市场需求增长 85%', 'TikTok', Colors.blue),
        ],
      ),
    );
  }

  Widget _trendItem(String title, String desc, String source, Color color) {
    return Container(
      margin: EdgeInsets.only(bottom: 12),
      padding: EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.03),
        borderRadius: BorderRadius.circular(16),
      ),
      child: Row(
        children: [
          Container(
            padding: EdgeInsets.all(10),
            decoration: BoxDecoration(color: color.withOpacity(0.1), borderRadius: BorderRadius.circular(12)),
            child: Text(source, style: TextStyle(color: color, fontWeight: FontWeight.bold, fontSize: 10)),
          ),
          SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
                Text(desc, style: TextStyle(color: Colors.white38, fontSize: 12)),
              ],
            ),
          ),
          Icon(Icons.arrow_forward_ios, size: 12, color: Colors.white24),
        ],
      ),
    );
  }
}
