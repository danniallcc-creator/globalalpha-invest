import 'package:flutter/material.dart';
import 'compass_result_screen.dart';
import 'compliance_detail_screen.dart';
import 'profile_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('跨境出海智库'),
        centerTitle: true,
        leading: IconButton(icon: Icon(Icons.person_outline), onPressed: () {
          Navigator.push(context, MaterialPageRoute(builder: (c) => ProfileScreen()));
        }),
        actions: [
          IconButton(icon: Icon(Icons.notifications_none), onPressed: () {}),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            _buildMarketTicker(),
            _buildSearchBar(),
            _buildFeatureGrid(context),
            _buildHotTrends(),
          ],
        ),
      ),
    );
  }

  Widget _buildMarketTicker() {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 8, horizontal: 16),
      color: Colors.black26,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text('伦敦金: $2,345.67 (+0.5%)', style: TextStyle(color: Colors.amber, fontSize: 12)),
          Text('USD/CNY: 7.24', style: TextStyle(color: Colors.white70, fontSize: 12)),
        ],
      ),
    );
  }

  Widget _buildSearchBar() {
    return Padding(
      padding: EdgeInsets.all(16.0),
      child: TextField(
        decoration: InputDecoration(
          hintText: '输入类目查询全球机会...',
          prefixIcon: Icon(Icons.search),
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(30)),
          filled: true,
          fillColor: Colors.white10,
        ),
      ),
    );
  }

  Widget _buildFeatureGrid(BuildContext context) {
    return GridView.count(
      shrinkWrap: true,
      physics: NeverScrollableScrollPhysics(),
      crossAxisCount: 2,
      padding: EdgeInsets.all(16),
      children: [
        GestureDetector(
          onTap: () => Navigator.push(context, MaterialPageRoute(builder: (c) => CompassResultScreen(category: "户外储能"))),
          child: _featureCard('消费地图罗盘', Icons.explore, Colors.blue),
        ),
        _featureCard('国别智库', Icons.book, Colors.green),
        GestureDetector(
          onTap: () => Navigator.push(context, MaterialPageRoute(builder: (c) => ComplianceDetailScreen())),
          child: _featureCard('合规查询', Icons.gavel, Colors.orange),
        ),
        _featureCard('AI 选品', Icons.auto_awesome, Colors.purple),
      ],
    );
  }

  Widget _featureCard(String title, IconData icon, Color color) {
    return Card(
      color: Colors.white.withOpacity(0.05),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 40, color: color),
          SizedBox(height: 8),
          Text(title, style: TextStyle(fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }

  Widget _buildHotTrends() {
    return Padding(
      padding: EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('实时选品趋势', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 12),
          ListTile(
            leading: CircleAvatar(child: Text('AMZ')),
            title: Text('便携储能电池'),
            subtitle: Text('德国站搜索量飙升 120%'),
            trailing: Icon(Icons.trending_up, color: Colors.green),
          ),
        ],
      ),
    );
  }
}
