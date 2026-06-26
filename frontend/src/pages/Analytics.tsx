import React from 'react';
import { TrendingUp, BarChart3, DollarSign, Target } from 'lucide-react';
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from 'recharts';

const Analytics: React.FC = () => {
  const applicationData = [
    { month: 'Jan', applications: 4, interviews: 2 },
    { month: 'Feb', applications: 8, interviews: 3 },
    { month: 'Mar', applications: 12, interviews: 5 },
    { month: 'Apr', applications: 15, interviews: 6 },
    { month: 'May', applications: 18, interviews: 8 },
    { month: 'Jun', applications: 22, interviews: 10 }
  ];

  const skillsData = [
    { skill: 'Python', proficiency: 90, demand: 95 },
    { skill: 'JavaScript', proficiency: 85, demand: 92 },
    { skill: 'React', proficiency: 88, demand: 89 },
    { skill: 'PostgreSQL', proficiency: 82, demand: 85 },
    { skill: 'Docker', proficiency: 75, demand: 88 }
  ];

  const stats = [
    {
      label: 'Total Applications',
      value: '22',
      change: '+12%',
      icon: TrendingUp,
      color: 'bg-blue-500'
    },
    {
      label: 'Interviews Scheduled',
      value: '10',
      change: '+5',
      icon: Target,
      color: 'bg-green-500'
    },
    {
      label: 'Average Match Score',
      value: '82%',
      change: '+5%',
      icon: BarChart3,
      color: 'bg-purple-500'
    },
    {
      label: 'Avg Salary Range',
      value: '$150k',
      change: '+$10k',
      icon: DollarSign,
      color: 'bg-orange-500'
    }
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Analytics & Insights</h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {stats.map((stat, idx) => {
          const Icon = stat.icon;
          return (
            <div key={idx} className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-600 dark:text-gray-400 text-sm">{stat.label}</p>
                  <p className="text-3xl font-bold text-gray-900 dark:text-white mt-2">{stat.value}</p>
                  <p className="text-green-600 dark:text-green-400 text-xs mt-1">{stat.change} this month</p>
                </div>
                <div className={`${stat.color} p-3 rounded-lg`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Applications Over Time */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Applications & Interviews</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={applicationData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="applications" stroke="#3b82f6" />
              <Line type="monotone" dataKey="interviews" stroke="#10b981" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Skills Analysis */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Skills: Your Level vs Market Demand</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={skillsData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="skill" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="proficiency" fill="#3b82f6" name="Your Proficiency" />
              <Bar dataKey="demand" fill="#f97316" name="Market Demand" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Insights */}
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Key Insights</h2>
        <div className="space-y-3">
          <div className="p-3 bg-blue-50 dark:bg-blue-900 rounded-lg">
            <p className="text-blue-900 dark:text-blue-100 text-sm">✓ Your match score has improved 5% this month. Keep optimizing your resume!</p>
          </div>
          <div className="p-3 bg-green-50 dark:bg-green-900 rounded-lg">
            <p className="text-green-900 dark:text-green-100 text-sm">✓ Interview conversion rate is 45%. Above average! Continue this momentum.</p>
          </div>
          <div className="p-3 bg-orange-50 dark:bg-orange-900 rounded-lg">
            <p className="text-orange-900 dark:text-orange-100 text-sm">⚠ Consider learning Kubernetes - it's in 88% of job postings you're targeting.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
