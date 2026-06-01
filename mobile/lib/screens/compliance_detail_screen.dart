import 'package:flutter/material.dart';

class ComplianceDetailScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: Text('合规百科'),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Color(0xFF020B18), Color(0xFF0D1B2A)],
          ),
        ),
        child: ListView(
          padding: EdgeInsets.fromLTRB(20, kToolbarHeight + 40, 20, 20),
          children: [
            _buildCategoryHeader('便携式储能系统'),
            SizedBox(height: 24),
            _buildComplianceCard('准入红线 (Redline)', [
              '欧盟：必须符合 CE-EMC, LVD, RoHS 指令',
              '美国：UL 2743 (便携式电源) 强制认证',
              '海运：必须持有 UN38.3 报告及 MSDS',
            ], Colors.redAccent, Icons.warning_amber_rounded),
            _buildComplianceCard('转型建议 (Insight)', [
              '放弃低毛利单机，开发含太阳能充电板的“户外应急套餐”',
              '针对寒冷地区增加自加热电池技术',
              '配备移动 APP 远程管理功能，提高溢价',
            ], Colors.greenAccent, Icons.lightbulb_outline),
            _buildActionCard(),
          ],
        ),
      ),
    );
  }

  Widget _buildCategoryHeader(String title) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
        SizedBox(height: 8),
        Text('已为您匹配 2026 全球核心经济体认证标准', style: TextStyle(color: Colors.white38)),
      ],
    );
  }

  Widget _buildComplianceCard(String title, List<String> items, Color color, IconData icon) {
    return Container(
      margin: EdgeInsets.only(bottom: 24),
      padding: EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.03),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: color.withOpacity(0.2)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, color: color, size: 24),
              SizedBox(width: 12),
              Text(title, style: TextStyle(fontSize: 18, color: color, fontWeight: FontWeight.bold)),
            ],
          ),
          SizedBox(height: 20),
          ...items.map((e) => Padding(
            padding: EdgeInsets.only(bottom: 12),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: EdgeInsets.only(top: 6),
                  child: Container(width: 4, height: 4, decoration: BoxDecoration(color: color, shape: BoxShape.circle)),
                ),
                SizedBox(width: 12),
                Expanded(child: Text(e, style: TextStyle(fontSize: 15, color: Colors.white70, height: 1.5))),
              ],
            ),
          )).toList(),
        ],
      ),
    );
  }

  Widget _buildActionCard() {
    return Container(
      padding: EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.blueAccent.withOpacity(0.1),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.blueAccent.withOpacity(0.2)),
      ),
      child: Row(
        children: [
          Icon(Icons.headset_mic_outlined, color: Colors.blueAccent, size: 32),
          SizedBox(width: 20),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('需要深度认证服务？', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                Text('一键联系专属合规专家', style: TextStyle(color: Colors.white54, fontSize: 13)),
              ],
            ),
          ),
          Icon(Icons.arrow_forward_ios, size: 16, color: Colors.white24),
        ],
      ),
    );
  }
}
